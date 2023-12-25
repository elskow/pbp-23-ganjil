from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def index(request):
    return render(request, "index.html")


def show_watchlist(request):
    watchlist_data = MyWatchList.objects.all()
    return render(request, "mywatchlist.html", {"watchlist_data": watchlist_data})


def show_json_watchlist(request):
    watchlist_data = MyWatchList.objects.all()
    data = serializers.serialize("json", watchlist_data)
    return HttpResponse(data, content_type="application/json")


def show_xml_watchlist(request):
    watchlist_data = MyWatchList.objects.all()
    data = serializers.serialize("xml", watchlist_data)
    return HttpResponse(data, content_type="application/xml")


def show_json_by_id(request, id):
    watchlist_data = MyWatchList.objects.filter(id=id)
    data = serializers.serialize("json", watchlist_data)
    return HttpResponse(data, content_type="application/json")


def show_xml_by_id(request, id):
    watchlist_data = MyWatchList.objects.filter(id=id)
    data = serializers.serialize("xml", watchlist_data)
    return HttpResponse(data, content_type="application/xml")
