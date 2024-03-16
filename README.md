# Oklahoma Earthquakes

Python project to list and/or visualize locations and details about recent Oklahoma earthquakes using USGS’s Earthquake Catalog ([API documentation](https://earthquake.usgs.gov/fdsnws/event/1/)) or [Oklahoma Geological Survey Earthquake Catalog Download Tool](https://ogsweb.ou.edu/eq_catalog/)

Inspired by [Oklahoma Cooling Centers Python Project](https://github.com/alex-code4okc/oklahoma_cooling_centers_python)

## Possible dependencies

* `requests`
* `pandas`
* `folium`

## First milestone:

* Grab last ~~7~~ 30 days of Oklahoma earthquakes ~~as a static csv~~ DONE
  * Chioma
* Read into `pandas` DataFrame DONE
  * Ruth/Amanda
* Clean up
  * Ruth
* Pipe into `folium`
  * Crystal
* Deploy (Netlify? GitHub Pages? Render?)
  * Crystal

## Instructions

* Install [Python3](https://www.python.org/downloads/)
* Create a virtual environment and install dependencies
    ```shell
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install -r requirements.txt
    ```
* Run the script
    ```shell
    python3 make_map.py
    ```
* Open the map in your browser
  * macOS
    ```shell
    open ./pages/index.html
    ```
  * Windows and Linux
    * Double-click the `index.html` file in your file manager
* Deactivate virtual environment
    ```shell
    deactivate
    ```

## Development

### Setup

* Follow the [instructions](#instructions) above to set up your environment
* Install [devbox](https://www.jetpack.io/devbox/docs/quickstart/)
    ```bash
    curl -fsSL https://get.jetpack.io/devbox | bash
    ```

### Usage

* Basic commands
    ```bash
    # install dependencies
    devbox install

    # enter devbox
    devbox shell

    # refresh devbox after making changes to devbox.json
    refresh

    # deactivate devbox
    exit
    ```
