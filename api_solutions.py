import requests
import json
import profile


def my_ip():
    my_ip_response = requests.get('https://api.ipify.org?format=json')
    return my_ip_response.json()['ip']


def shorten(url):
    shorten_data = {
        'url': (str(url))  # make sure to url encode
    }
    shorten_response = requests.post('https://cleanuri.com/api/v1/shorten', data=shorten_data)
    return shorten_response.json()['result_url']


def send_file(file_name):
    files = {
        'file': (file_name, open(file_name, 'rb')),
    }

    file_response = requests.post('https://file.io/', files=files)
    return file_response.json()['link']


def make_profile():
    profile_response = requests.get('https://pipl.ir/v1/getPerson')
    profile_object = profile.profile_from_dict(profile_response.json()).person
    profile_object.personal.profile = "https://thispersondoesnotexist.com/image"
    return profile_object.to_dict()


def weather(address):
    location_response = requests.get(
        "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress" +
        "?address={}&benchmark=Public_AR_Current&format=json"
        .format(address)
    ).json()
    lat = location_response['result']['addressMatches'][0]['coordinates']['y']
    long = location_response['result']['addressMatches'][0]['coordinates']['x']
    weather_station_response = requests.get("https://api.weather.gov/points/{},{}".format(lat, long)).json()
    weather_response = requests.get(weather_station_response['properties']['forecast']).json()
    return weather_response['properties']['periods']


if __name__ == '__main__':
    print("My IP: " + str(my_ip()))
    print("Shortened link: " + str(shorten("https://www.apple.com/")))
    print("File link" + str(send_file("sample_file.txt")))
    print(json.dumps(make_profile(), indent=2))
    print(json.dumps(weather("11 Wall St, New York, NY 10005"), indent=2))
