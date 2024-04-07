#!/usr/bin/env python

import folium
import json
from datetime import datetime
from urllib.parse import urlencode
from urllib.request import urlopen
from zoneinfo import ZoneInfo

# env vars
BASE_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"
COLORS = {(0.0, 1.0): "yellow", (1.0, 2.0): "red", (2.0, 3.0): "black", (3.0, float("inf")): "blue"}

COLORS = {
    (0, 1): "lightgray",
    (1, 2): "blue",
    (2, 3): "green",
    (3, 4): "purple",
    (4, 5): "orange",
    (5, 6): "red",
    (6, float("inf")): "pink",
}


def assign_color_by_mag(mag):
    for range_, color in COLORS.items():
        if range_[0] <= mag < range_[1]:
            return color
    return "white"


def convert_epoch_to_central(time):
    dt = datetime.fromtimestamp(time / 1000, tz=ZoneInfo("America/Chicago"))
    return dt.strftime("%d %b %Y %I:%M%p")


def get_earthquakes():
    payload = {"format": "geojson", "catalog": "ok", "eventtype": "earthquake"}
    qs = urlencode(payload)

    response = urlopen(f"{BASE_URL}?{qs}")
    js = json.loads(response.read())

    for feature in js["features"]:
        feature["properties"]["time"] = convert_epoch_to_central(feature["properties"]["time"])

    return js


def main():
    quakes = get_earthquakes()

    ok_map = folium.Map(location=[35.4823241, -97.7593895], zoom_start=7)

    folium.GeoJson(
        quakes,
        marker=folium.CircleMarker(),
        popup=folium.GeoJsonPopup(fields=["time", "mag", "place"], aliases=["Time", "Magnitude", "Location"]),
        tooltip=folium.GeoJsonTooltip(fields=["time", "mag", "place"], aliases=["Time", "Magnitude", "Location"]),
        style_function=lambda feature: {
            "color": "black",
            "weight": 1,
            "radius": feature["properties"]["mag"] * 3.5,
            "fill": True,
            "fillColor": assign_color_by_mag(feature["properties"]["mag"]),
        },
    ).add_to(ok_map)

    ok_map.save("pages/index.html")


if __name__ == "__main__":
    main()
