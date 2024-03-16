#!/usr/bin/env python

from urllib.parse import urlencode

import folium
import pandas as pd

BASE_URL='https://earthquake.usgs.gov/fdsnws/event/1/query'

def get_data():
    payload={'format':'csv', 'catalog':'ok', 'eventtype':'earthquake'}
    qs = urlencode(payload)

    df =pd.read_csv(f'{BASE_URL}?{qs}', usecols=['latitude', 'longitude', 'place', 'time', 'mag'], header=0)
    df['time'] = pd.to_datetime(df['time'])
    df['time'] = df['time'].dt.tz_convert('US/Central')
    df['date'], df['time'] = df['time'].dt.date, df['time'].dt.time
    return df

def icon_by_magnitude(mag):
    if mag < 1:
        color = 'red'
    elif 1 <= mag < 2:
        color = 'orange'
    elif 2 <= mag < 3:
        color = 'pink'
    elif 3 <= mag < 4:
        color = 'green'
    elif 4 <= mag < 5:
        color = 'blue'
    elif 5 <= mag < 6:
        color = 'purple'
    elif 6 <= mag:
        color = 'white'
    else:
        color = 'black'

    return folium.Icon(color=color)

def add_markers(df, map):
    # TODO: Fix zip
    for place, mag, lat, lon, date, time in zip(df['place'], df['mag'], df['latitude'], df['longitude'], df['date'], df['time']):
        latF = float(lat)
        lonF = float(lon)
        icon = icon_by_magnitude(mag)
        folium.Marker([latF, lonF],icon=icon, popup=f'<div><p>Date: {date}</p><p>Time: {time}</p><p>Place: {place}</p><p>Mag: {mag}</p></div>', tooltip=place).add_to(map)
        folium.Marker([latF, lonF])

def main():
    earthquake_df = get_data()
    ok_map = folium.Map(location=[35.4823241,-97.7593895], zoom_start=7)
    add_markers(earthquake_df, ok_map)
    ok_map.save('pages/index.html')

if __name__=='__main__':
    main()
