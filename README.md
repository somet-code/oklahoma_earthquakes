# Oklahoma Earthquakes

Python project to list and/or visualize locations and details about recent Oklahoma earthquakes using USGS’s Earthquake Catalog ([API documentation](https://earthquake.usgs.gov/fdsnws/event/1/)) or [Oklahoma Geological Survey Earthquake Catalog Download Tool](https://ogsweb.ou.edu/eq_catalog/)

Inspired by [Oklahoma Cooling Centers Python Project](https://github.com/alex-code4okc/oklahoma_cooling_centers_python)

## Possible dependencies
* Requests
* pandas
* Folium

## First milestone:
* Grab last 7 days of Oklahoma earthquakes as a static csv
  * Chioma
* Read into pandas DataFrame
  * Ruth/Amanda
* Clean up?
  * Ruth
* Pipe into Folium
  * Crystal
* Deploy (Netlify? GitHub Pages? Render?)
  * Crystal

## Instructions

```shell
# ****** Mac Terminal ******
# create virtual environment 
python3 -m venv .venv
# activate virtual environment
source .venv/bin/activate
# install dependencies
python3 -m pip install -r requirements.txt
# run script
python3 makeMap.py
# open map in browser
open ./pages/index.html
# deactivate virtual environment
deactivate


## ****** Windows ******
```shell
# create virtual environment 
python -m venv .venv
# activate virtual environment
venv/bin/activate
# install dependencies
python -m pip install -r requirements.txt
# run script
python makeMap.py
# open map in browser
open ./pages/index.html
# deactivate virtual environment
deactivate
```
