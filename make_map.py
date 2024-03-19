#!/usr/bin/env python

from urllib.parse import urlencode

import folium
import pandas as pd

BASE_URL='https://earthquake.usgs.gov/fdsnws/event/1/query'

COLORS = {
    (0, 1): 'lightgray',
    (1, 2): 'blue',
    (2, 3): 'green',
    (3, 4): 'purple',
    (4, 5): 'orange',
    (5, 6): 'red',
    (6, float('inf')): 'pink'
}

def get_data():
    payload={'format':'csv', 'catalog':'ok', 'eventtype':'earthquake'}
    qs = urlencode(payload)

    df =pd.read_csv(f'{BASE_URL}?{qs}', usecols=['time','latitude', 'longitude', 'place', 'mag'], header=0)
    df['time'] = pd.to_datetime(df['time']).dt.tz_convert('US/Central')
    df['date'], df['time'] = df['time'].dt.date, df['time'].dt.time
    return df

def assign_color(mag):
    for range_, color in COLORS.items():
        if range_[0] <= mag < range_[1]:
            return color
    return 'white'

def make_custom_icon(mag):
    color = assign_color(mag)
    return folium.Icon(color=color)

def make_custom_marker(s):
    icon = make_custom_icon(s['mag'])
    return folium.Marker([s['latitude'], s['longitude']], icon=icon, popup=f"<div><p>Date: {s['date']}</p><p>Time: {s['time']}</p><p>Place: {s['place']}</p><p>Mag: {s['mag']}</p></div>", tooltip=s['place'])

def setup_markers(df):
    df['marker'] = df.apply(make_custom_marker, axis=1)

def add_markers(df, fmap):
    for marker in df['marker']:
        marker.add_to(fmap)

def main():
    earthquake_df = get_data()
    setup_markers(earthquake_df)
    ok_map = folium.Map(location=[35.4823241,-97.7593895], zoom_start=7)
    add_markers(earthquake_df, ok_map)
    ok_map.save('pages/index.html')

if __name__=='__main__':
    main()
