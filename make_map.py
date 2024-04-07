#!/usr/bin/env python

from datetime import date, datetime, timedelta
import json
from urllib.parse import urlencode
from urllib.request import urlopen
from zoneinfo import ZoneInfo

from flask import Flask, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
import folium

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


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

class EarthquakeForm(FlaskForm):
    startday = SelectField('Days before present',
                           choices=[(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7)],
                           coerce=int
                           )
    minmag = SelectField('Minimum magnitude',
                         choices=[(0,0), (1,1), (2,2), (3,3), (4,4), (5,5)],
                         coerce=int
                         )
    submit = SubmitField('Get earthquakes')

def assign_color_by_mag(mag):
    for range_, color in COLORS.items():
        if range_[0] <= mag < range_[1]:
            return color
    return 'white'

def convert_epoch_to_central(time):
    dt = datetime.fromtimestamp(time/1000, tz=ZoneInfo('America/Chicago'))
    return dt.strftime('%d %b %Y %I:%M%p')

def get_earthquakes(state='ok', starttime=date.today()-timedelta(7), minmagnitude=0):
    payload={'format': 'geojson',
             'catalog': state,
             'starttime': starttime,
             'minmagnitude': minmagnitude,
             'eventtype': 'earthquake'}
    qs = urlencode(payload)
    
    response = urlopen(f'{BASE_URL}?{qs}')
    js = json.loads(response.read())

    for feature in js['features']:
        feature['properties']['time'] = convert_epoch_to_central(feature['properties']['time'])

    return js

def make_earthquake_map(state='ok', starttime=date.today()-timedelta(7), minmagnitude=0):
    quakes = get_earthquakes(state, starttime, minmagnitude)

    ok_map = folium.Map(location=[35.5,-98.7], zoom_start=7)

    folium.GeoJson(quakes,
               marker=folium.CircleMarker(),
               popup=folium.GeoJsonPopup(fields=['time','mag','place'],
                                         aliases=['Time','Magnitude','Location']
                                        ),
               tooltip=folium.GeoJsonTooltip(fields=['time','mag','place'],
                                         aliases=['Time','Magnitude','Location']
                                        ),
               style_function = lambda feature: {
                   'color': 'black',
                   'weight': 1,
                   'radius': feature['properties']['mag']*3.5,
                   'fill': True,
                   'fillColor': assign_color_by_mag(feature['properties']['mag'])
               }
              ).add_to(ok_map)

    return ok_map.get_root().render()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EarthquakeForm(startday=7, minmag=0)

    iframe = make_earthquake_map()

    if form.validate_on_submit():
        iframe = make_earthquake_map(starttime=date.today()-timedelta(form.startday.data),
                                     minmagnitude=form.minmag.data
                                     )
        #form = EarthquakeForm(formdata=None)
    
    return render_template('index.html', form=form, iframe=iframe)

if __name__=='__main__':
    app.run(debug=True)