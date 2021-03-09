import requests
import json


def my_ip():
    pass


def shorten(url):
    pass


def send_file(file_name):
    pass


def make_profile():
    pass


def weather(address):
    pass


if __name__ == '__main__':
    print("My IP: " + str(my_ip()))
    print("Shortened link: " + str(shorten("https://www.apple.com/")))
    print("File link" + str(send_file("sample_file.txt")))
    print(json.dumps(make_profile(), indent=2))
    print(json.dumps(weather("11 Wall St, New York, NY 10005"), indent=2))
