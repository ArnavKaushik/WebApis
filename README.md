# WebApis
Practice using REST APIs with Python and visualize the results with Flask.

# Setup
This project requires Python 3 to be installed on your computer. Please verify that you also have `pip` installed.
## Download Source
To begin using this practice project, please download the code.
You can also use `git clone https://github.com/ArnavKaushik/WebApis.git`.

## Install Dependencies
This project needs the following dependencies:
```
requests
Flask
```

There are two ways of installing these for this project:
1. Use `pip install` or `pip3 install`
2. Use `pip install -r` or `pip3 install -r`

For the first option, run the correct two commands:
```
# If using pip
pip install requests
pip install Flask

# If using pip3
pip3 install requests
pip3 install requests
```

For the second option, run the correct command:
```
# If using pip
pip install -r requirements.txt

# If using pip3
pip3 install -r requirements.txt
```

# Using the project
The primary purpose of the project is to learn how to use python to make requests to free and publicly available APIs.

The file [`api.py`](https://github.com/ArnavKaushik/WebApis/blob/main/api.py) contains comments that act as a guide. 

In order to use the visualization functionality, you must complete the functions in [`api.py`](https://github.com/ArnavKaushik/WebApis/blob/main/api.py) or change the import located in [`visualize.py`](https://github.com/ArnavKaushik/WebApis/blob/main/visualize.py#L2) to `import api_solutions as api`.

The [`api_minified.py`](https://github.com/ArnavKaushik/WebApis/blob/main/api_minified.py) file serves as a bare version of [`api.py`](https://github.com/ArnavKaushik/WebApis/blob/main/api.py). If you would like to use this file for the visualization, change the import located in [`visualize.py`](https://github.com/ArnavKaushik/WebApis/blob/main/visualize.py#L2) to `import api_minified as api`. 


# Credits
Thank you to the following sites for providing these free and publicly available APIs. The purpose of this project is purely educational, and would not be possible without these them. If you use this project, you agree to be considerate with your API usage and agree not to abuse these services.

* [ipify](https://www.ipify.org/)
* [cleanuri](https://cleanuri.com/)
* [file.io](https://www.file.io/)
* [pipl.ir](https://pipl.ir/)
* [thispersondoesnotexist.com](https://thispersondoesnotexist.com)
* [US Census Bureau](https://geocoding.geo.census.gov/)
* [National Weather Service](https://api.weather.gov/)

WebApis is licensed under the MIT License. Please read [LICENSE](https://github.com/ArnavKaushik/WebApis/blob/main/LICENSE) for more details.
