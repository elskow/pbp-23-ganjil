from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import get_object_or_404
from todolist.models import Task


# Custom user creation form with username and password validation
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput,
        validators=[validate_password],
        label="Password",
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


# Register view
def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Account created successfully")
        return redirect("todolist:login")
    return render(request, "register.html", {"form": form})


# Login view
def login_user(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("todolist:home")
        messages.error(request, "Invalid username or password")
    return render(request, "login.html")


# Logout view
@login_required(login_url="todolist:login")
def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect("todolist:login")


# Home view
@login_required(login_url="todolist:login")
def home(request):
    tasks = request.user.task_set.all().order_by("is_finished", "-date")
    return render(request, "home.html", {"tasks": tasks, "time": datetime.now()})


# Add task view
@login_required(login_url="todolist:login")
def add_task(request):
    if request.method == "POST" and request.POST["title"]:
        request.user.task_set.create(
            title=request.POST["title"],
            description=request.POST["description"],
            date=datetime.now().date(),
        )
        messages.success(request, "Task added successfully")
        return redirect("todolist:home")
    messages.error(request, "Task title cannot be empty")
    return redirect("todolist:home")


# Delete task view
@login_required(login_url="todolist:login")
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully")
    return redirect("todolist:home")


# Toggle task finished status view
@login_required(login_url="todolist:login")
def toggle_finished(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.is_finished = "is_finished" in request.POST
        task.save()
        messages.success(request, "Task updated successfully")
        return redirect("todolist:home")
    return render(request, "home.html", {"tasks": request.user.task_set.all()})
