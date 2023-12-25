import datetime
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from wishlist.models import BarangWishlist


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Akun berhasil dibuat")
            return redirect("wishlist:login")

    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, "Username atau Password salah!")
    context = {}
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("wishlist:login"))
    response.delete_cookie("last_login")
    return redirect("wishlist:login")


@login_required(login_url="wishlist:login")
def show_wishlist(request):
    data_barang = BarangWishlist.objects.all()
    context = {
        "list_barang": data_barang,
        "nama": "Saya",
        "last_login": request.COOKIES.get("last_login"),
    }
    return render(request, "wishlist.html", context)


def show_json(request):
    data_barang = BarangWishlist.objects.all()
    data_json = serializers.serialize("json", data_barang)
    return HttpResponse(data_json, content_type="application/json")


def show_xml(request):
    data_barang = BarangWishlist.objects.all()
    data_xml = serializers.serialize("xml", data_barang)
    return HttpResponse(data_xml, content_type="application/xml")


def show_json_by_id(request, id):
    data_barang = BarangWishlist.objects.filter(id=id)
    data_json = serializers.serialize("json", data_barang)
    return HttpResponse(data_json, content_type="application/json")


def show_xml_by_id(request, id):
    data_barang = BarangWishlist.objects.filter(id=id)
    data_xml = serializers.serialize("xml", data_barang)
    return HttpResponse(data_xml, content_type="application/xml")
