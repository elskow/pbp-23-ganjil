from django.urls import path
from mywatchlist.views import (
    index,
    show_watchlist,
    show_json_watchlist,
    show_xml_watchlist,
    show_json_by_id,
    show_xml_by_id,
)

app_name = "mywatchlist"

urlpatterns = [
    path("", index, name="index"),
    path("html/", show_watchlist, name="show_watchlist"),
    path("json/", show_json_watchlist, name="show_json_watchlist"),
    path("xml/", show_xml_watchlist, name="show_xml_watchlist"),
    path("json/<int:id>", show_json_by_id, name="show_json_by_id"),
    path("xml/<int:id>", show_xml_by_id, name="show_xml_by_id"),
]
