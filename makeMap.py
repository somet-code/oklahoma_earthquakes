import requests
import pandas as pd

BASE_URL='https://earthquake.usgs.gov/fdsnws/event/1/query'

def get_data():
    payload={'format':'csv', 'catalog':'ok', 'eventtype':'earthquake'}
    response = requests.get(BASE_URL,params=payload)

    df =pd.read_csv(response.url, usecols=['latitude', 'longitude', 'place', 'time', 'mag'])
    df['time'] = pd.to_datetime(df['time'])
    df['time'] = df['time'].dt.tz_convert('US/Central')
    df['date'], df['time'] = df['time'].dt.date, df['time'].dt.time
    
    print(df.head())

if __name__=='__main__':
    get_data()
