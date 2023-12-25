from django.db import models


class BarangWishlist(models.Model):
    nama_barang = models.CharField(max_length=255)
    harga_barang = models.IntegerField()
    deskripsi = models.TextField()
