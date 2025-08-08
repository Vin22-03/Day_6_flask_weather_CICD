from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = '21ed352bcc8c40539da155457250408'  # replace with real one
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

    try:
        response = requests.get(url).json()

        if "error" in response:
            return f"<p>City not found: {city}</p><a href='/'>Try Again</a>"

        temp = response['current']['temp_c']
        desc = response['current']['condition']['text']
        return render_template("result.html", city=city, temp=temp, desc=desc)

    except Exception as e:
        return f"<p>Error: {e}</p>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

