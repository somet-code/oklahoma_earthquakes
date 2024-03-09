import requests
import pandas as pd
import folium

BASE_URL='https://earthquake.usgs.gov/fdsnws/event/1/query'

def get_data():
    payload={'format':'csv', 'catalog':'ok', 'eventtype':'earthquake'}
    response = requests.get(BASE_URL,params=payload)

    df =pd.read_csv(response.url, usecols=['latitude', 'longitude', 'place', 'time', 'mag'], header=0)
    df['time'] = pd.to_datetime(df['time'])
    df['time'] = df['time'].dt.tz_convert('US/Central')
    df['date'], df['time'] = df['time'].dt.date, df['time'].dt.time
    return df
  

if __name__=='__main__':
    earthquake_df = get_data()
    ok_map = folium.Map(location=[35.4823241,-97.7593895], zoom_start=7)

    for place, mag, lat, lon, date, time in zip(earthquake_df['place'], earthquake_df['mag'], earthquake_df['latitude'], earthquake_df['longitude'], earthquake_df['date'], earthquake_df['time']):
        latF = float(lat)
        lonF = float(lon)
        folium.Marker([latF, lonF], popup=f'<div><p>Date: {date}</p><p>Time: {time}</p><p>Place: {place}</p><p>Mag: {mag}</p></div>', tooltip=place).add_to(ok_map)
    
    ok_map.save('pages/index.html')   
