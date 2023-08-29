
import requests
import json
from flask import Flask

app = Flask(__name__)


@app.route('/get_coordinates/<location>')
def get_coordinates(location):
    api_key = "be3eb6c5d1e94fac9ea22e74a3c23ac7"
    url = f"https://api.opencagedata.com/geocode/v1/json?key={api_key}&q={location}"

    response = requests.get(url)
    data = response.json()
    coordinates = data['results'][0]['geometry']
    return coordinates

if __name__ == '__main__':
    app.run()

