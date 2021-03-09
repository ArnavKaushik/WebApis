from flask import Flask, render_template, request
import api as api
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/tmp"


@app.route('/')
@app.route('/api/')
def index():
    return render_template('index.html')


@app.route('/api/my_ip')
def get_my_ip():
    my_ip = api.my_ip()
    print(my_ip)
    return render_template('my_ip.html', ip=my_ip)


@app.route('/api/shorten', methods=['GET', 'POST'])
def shorten():
    if request.method == "POST":
        if len(request.form["url"]) > 0:
            shortened_link = api.shorten(request.form["url"])
            return render_template('shortened.html', link=shortened_link)
        else:
            return render_template('shorten.html')
    else:
        return render_template('shorten.html')


@app.route('/api/send_file', methods=['GET', 'POST'])
def send_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('send_file.html')
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return render_template('send_file.html')
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_link = api.send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('send_file.html', link=file_link)
    else:
        return render_template('send_file.html')


@app.route('/api/make_profile')
def make_profile():
    profile = api.make_profile()
    if len(profile) > 0:
        return render_template('make_profile.html', person=profile, error="null")
    else:
        return render_template('make_profile.html', error="Invalid API")


@app.route('/api/weather', methods=['GET', 'POST'])
def weather():
    if request.method == "POST":
        if len(request.form['address']) > 0:
            weather_data = api.weather(str(request.form['address']).strip())
            if len(weather_data) > 0:
                return render_template('weather_result.html', address=str(request.form['address']).strip(),
                                       weather=weather_data, error="null")
            else:
                return render_template('weather_result.html', error="Please input a valid address.")
        else:
            return render_template('weather.html')
    else:
        return render_template('weather.html')


if __name__ == '__main__':
    app.run(debug=True)
