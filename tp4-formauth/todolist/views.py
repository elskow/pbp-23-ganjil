from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import get_object_or_404
from todolist.models import Task


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        validators=[
            # Custom validator
        ],
    )
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
        user = super(CustomUserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user


def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("todolist:login")

    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("todolist:home")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


@login_required(login_url="todolist:login")
def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect("todolist:login")


@login_required(login_url="todolist:login")
def home(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        date = datetime.now().date()
        user = request.user

        if title != "":
            user.task_set.create(title=title, description=description, date=date)
            messages.success(request, "Task added successfully")
        else:
            messages.error(request, "Task title cannot be empty")

    tasks = request.user.task_set.all().order_by("-date")
    context = {"tasks": tasks, "time": datetime.now()}
    return render(request, "home.html", context)


@login_required(login_url="todolist:login")
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully")
        return redirect("todolist:home")
    return redirect("todolist:home")


@login_required(login_url="todolist:login")
def toggle_finished(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.is_finished = "is_finished" in request.POST
        task.save()
        messages.success(request, "Task updated successfully")
        print("Task updated successfully")
        return redirect("todolist:home")
    print("Task not updated successfully")
    return render(request, "toggle_finished.html", {"task": task})
