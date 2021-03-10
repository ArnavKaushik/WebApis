import requests
import json
import profile

"""
Disclaimer: 
    Do not use a broad try/except statement in production. 
    The purpose of the try/except statement is to find errors and prevent them from ruining the program.
    Avoiding any and all errors is not a good idea.
"""


def my_ip():
    try:
        my_ip_response = requests.get('https://api.ip.sb/jsonip')
        if my_ip_response.status_code == 200:
            return my_ip_response.json()['ip']
        else:
            return "Invalid API"
    except:
        return "Invalid API"


def shorten(url):
    try:
        shorten_data = {
            'url': (str(url))  # make sure to url encode
        }
        shorten_response = requests.post('https://cleanuri.com/api/v1/shorten', data=shorten_data)
        if shorten_response.status_code == 200:
            return shorten_response.json()['result_url']
        elif shorten_response.status_code == 400:
            return shorten_response.json()['error']
        else:
            return "Invalid API"
    except:
        return "Invalid API"


def send_file(file_name):
    try:
        files = {
            'file': (file_name, open(file_name, 'rb')),
        }

        file_response = requests.post('https://file.io/', files=files)
        if file_response.status_code == 200:
            return file_response.json()['link']
        else:
            if 'message' in file_response.json():
                return file_response.json()['message']
            else:
                return "Invalid API"
    except:
        return "Invalid API"


def make_profile():
    try:
        profile_response = requests.get('https://pipl.ir/v1/getPerson')
        if profile_response.status_code == 200:
            profile_object = profile.profile_from_dict(profile_response.json()).person
            profile_object.personal.profile = "https://thispersondoesnotexist.com/image"
            return profile_object.to_dict()
        else:
            return {}
    except:
        return {}


def weather(address):
    try:
        location_response = requests.get(
            "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress" +
            "?address={}&benchmark=Public_AR_Current&format=json"
            .format(address)
        )
        if location_response.status_code != 200:
            return []
        if len(location_response.json()['result']['addressMatches']) == 0:
            return []
        lat = location_response.json()['result']['addressMatches'][0]['coordinates']['y']
        long = location_response.json()['result']['addressMatches'][0]['coordinates']['x']
        weather_station_response = requests.get("https://api.weather.gov/points/{},{}".format(lat, long))
        if weather_station_response.status_code != 200:
            return []
        weather_response = requests.get(weather_station_response.json()['properties']['forecast'])
        if weather_response.status_code != 200:
            return []

        # Create CSV file from the data
        with open('tmp/weather_data.csv', 'w') as output:
            output.write(
                'id,name,startTime,endTime,temperature,temperatureUnit,windSpeed,windDirection,isDaytime,shortForecast,detailedForecast,icon\n'
            )
            periods = weather_response.json()['properties']['periods']
            for i in range(len(periods)):
                print(periods[i])
                output.write(
                    '{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(
                        periods[i]['number'],
                        periods[i]['name'],
                        periods[i]['startTime'],
                        periods[i]['endTime'],
                        periods[i]['temperature'],
                        periods[i]['temperatureUnit'],
                        periods[i]['windSpeed'],
                        periods[i]['windDirection'],
                        periods[i]['isDaytime'],
                        periods[i]['shortForecast'],
                        "\"" + str(periods[i]['detailedForecast']) + "\"",
                        "\"" + str(periods[i]['icon']) + "\""
                    )
                )

        return weather_response.json()['properties']['periods']
    except:
        return []


if __name__ == '__main__':
    print("My IP: " + str(my_ip()))
    print("Shortened link: " + str(shorten("https://www.apple.com/")))
    print("File link" + str(send_file("sample_file.txt")))
    print(json.dumps(make_profile(), indent=2))
    print(json.dumps(weather("11 Wall St, New York, NY 10005"), indent=2))
