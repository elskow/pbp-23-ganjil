from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from wishlist.models import BarangWishlist


def show_wishlist(request):
    data_barang = BarangWishlist.objects.all()
    context = {"list_barang": data_barang, "nama": "Saya"}
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
