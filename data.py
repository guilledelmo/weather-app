import requests
import geolocation


def make_request(import_latitude, import_longitude):
    api_params = {"lang": "en", "units": "si"}
    response = requests.get("https://api.darksky.net/forecast/397a0597fc3d061dcddaf1be6b61a035/{},{}".format(import_latitude, import_longitude), params=api_params)
    json_response = response.json()
    return json_response