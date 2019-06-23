from geopy.geocoders import Nominatim


def get_lat(user_location):
    geolocator = Nominatim(user_agent="test_app")
    location_one = geolocator.geocode(user_location)
    return location_one.latitude

def get_long(user_location):
    geolocator = Nominatim(user_agent="test_app")
    location_two = geolocator.geocode(user_location)
    return location_two.longitude

def get_info(user_location):
    geolocator = Nominatim(user_agent="test_app")
    location = geolocator.geocode(user_location)
    return ", ".join(location.address.split(", ")[-3:])