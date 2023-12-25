from django.shortcuts import render
from wishlist.models import BarangWishlist


def show_wishlist(request):
    data_barang = BarangWishlist.objects.all()
    context = {"list_barang": data_barang, "nama": "Saya"}
    return render(request, "wishlist.html", context)
