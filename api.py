"""
Welcome to Web APIs!
We'll be going over various APIs and how we can interact with them.

Notice:
    These APIs are for educational purposes only.
    These are free services, so please do not abuse them, specifically by spamming requests.
        There is a good chance you'll be denied multiple requests as these are commonly rate limited.

README:
    If you'd like to use this file without all the comments, open `api_minified.py`.
    View the solutions in `api_solutions.py`
"""

# ########################################### #
#                                             #
#             Importing Libraries             #
#                                             #
# ########################################### #

"""
Import the `requests` library.
This will be the library that we'll use to make our API requests.
"""
import requests

"""
Import the `json` library
This will be used to parse the data that we get pack.
"""
import json

"""
Alright, enough setup. Let's call some APIs!
"""

# ########################################### #
#                                             #
#                 Calling APIs                #
#                                             #
# ########################################### #

"""
We need to make sure we add error handling to our code. 
For example, if the API doesn't exist, we should handle the error by returning "Invalid API" or something like that.
Here are some common status codes:
    - 200: OK (Everything worked out!)
    - 400: Bad Request (The data and/or parameters might be messed up.)
    - 401: Unauthorized (None of our APIs here need keys, but keep this in mind.)
    - 404: Not Found (Check the URL and/or parameters?)
    - 405: Method Not Allowed (You might be using GET on a POST API, or something along those lines.)
    - 500: Internal Server Error (This is a server side error, so we can only hope it gets fixed.)
"""


# +-------------------------------------------+
# |                 Get My IP                 |
# |                   ip.sb                   |
# +-------------------------------------------+

"""
The purpose of this API is to learn about a GET request. 
This is a way to get your public IP back from an API.
"""


def my_ip():
    pass


# +-------------------------------------------+
# |                Link Shortner              |
# |                CleanURI.com               |
# +-------------------------------------------+

"""
The purpose of this API is to learn about a POST request. 
This is a way to create data via an API after either calling it or passing parameters.
In this case, we're asking the API to create a short link for us, and we'll get it back in the response.

Notice:
    This API has DDOS protection, so don't be alarmed if the shortened url shows a Cloudflare page.
"""


def shorten(url):
    pass


# +-------------------------------------------+
# |           Temporary File Storage          |
# |                  File.io                  |
# +-------------------------------------------+

"""
The purpose of this API is to continue learning about a POST request. 
This API allows us to send data through a temporary file sharing service.
We can send a file using the `file` parameter.
"""


def send_file(file_name):
    pass


"""
Let's try some more advanced APIs.
"""

# ########################################### #
#                                             #
#            Calling Advanced APIs            #
#                                             #
# ########################################### #


# +-------------------------------------------+
# |           Let's make a profile!           |
# |                 pipl.ir                   |
# |         thispersondoesnotexist.org        |
# +-------------------------------------------+

"""
This one is going to be a bit more complicated.
We're going to use a fake profile generator and generate an image using AI.
We need two APIs for this one:
    A profile generator from pipl.ir.
    An image from thispersondoesnotexist.com
"""


def make_profile():
    pass


# +-------------------------------------------+
# |             NWS Weather Data              |
# |          geocoding.geo.census.gov         |
# |              api.weather.gov              |
# +-------------------------------------------+

"""
This one is going to be the most complicated one in this file.
We're going to use the NWS weather data api to get the week's weather.
We need multiple APIs for this one:
    We need to convert an address to latitude and longitude via Census data
    We need to get the weather station for this latitude and longitude.
    We need to get the weather data from the forecast API provided by the previous API.
"""


def weather(address):
    pass


"""
That one was a bit trickier. 
"""

# ########################################### #
#                                             #
#                  Conclusion                 #
#                                             #
# ########################################### #

"""
Now that we have our API functions done, let's try to visualize the data.
Navigate to the `visualize.py` file and press run.

If you don't have Flask installed, run the correct command:
    If you have Python 3:
        pip3 install Flask
    If you don't know:
        pip install Flask
    If that doesn't work, try this if you haven't already:
        pip3 install Flask
    If that doesn't work:
        Search it up? (Psst! StackOverflow.com has every solution to every problem)
"""

if __name__ == '__main__':
    print("My IP: " + str(my_ip()))
    print("Shortened link: " + str(shorten("https://www.apple.com/")))
    print("File link" + str(send_file("sample_file.txt")))
    print(json.dumps(make_profile(), indent=2))
    print(json.dumps(weather("11 Wall St, New York, NY 10005"), indent=2))
