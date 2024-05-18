# Oklahoma Earthquakes

Python project to list and/or visualize locations and details about recent Oklahoma earthquakes using USGS’s Earthquake Catalog ([API documentation](https://earthquake.usgs.gov/fdsnws/event/1/))

Inspired by [Oklahoma Cooling Centers Python Project](https://github.com/alex-code4okc/oklahoma_cooling_centers_python)

## Dependencies

* `folium`
* `flask`

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
* Open the map in your browser at http://127.0.0.1:5000
* Deactivate virtual environment
    ```shell
    deactivate
    ```

## Development

### Devbox

* Follow the [instructions](#instructions) above to set up your environment
* Install [devbox](https://www.jetpack.io/devbox/docs/quickstart/)
    ```bash
    curl -fsSL https://get.jetpack.io/devbox | bash
    ```
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

### Pre-commit hooks

* Install [pre-commit](https://pre-commit.com/#install)
    ```bash
    # python
    python3 -m pip install pre-commit

    # homebrew
    brew install pre-commit
    ```
* Install pre-commit hooks
    ```bash
    pre-commit install
    ```
* Run pre-commit hooks
    ```bash
    pre-commit run --all-files
    ```
* Skip pre-commit hooks
    ```bash
    git commit -m "commit message" --no-verify
    ```
