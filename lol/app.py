from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Obținem adresa IP a clientului
    client_ip = request.remote_addr

    # Obținem informațiile despre țară folosind serviciul GeoJS
    response = requests.get(f"https://get.geojs.io/v1/ip/country/{client_ip}.json")
    data = response.json()
    country_code = data.get('country')

    # Definim textul în funcție de țară
    if country_code == "RO":
        greeting = "Bună ziua!"
    elif country_code == "US":
        greeting = "Hello!"
    elif country_code == "FR":
        greeting = "Hallo!"
    else:
        greeting = "Salut!"

    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
