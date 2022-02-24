from weakref import ref
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from rsa import PrivateKey
from flask import *
import json
import requests

from config import PORT
cred = credentials.Certificate('firebase-sdk.json')
app = Flask(__name__)
app.config["DEBUG"] = True
firebase_admin.initialize_app(cred, {

'databaseURL': 'https://weather-station-1514a-default-rtdb.firebaseio.com/'})

@app.route('/', methods=['GET'])
def home_page():

    Air_Quality = db.reference("Air_Quality").get()
    Altitude = db.reference("Altitude").get()
    Cng = db.reference("Cng").get()
    Humidity = db.reference("Humidity").get()
    Ldr = db.reference("Ldr").get()
    Lpg = db.reference("Lpg").get()
    Pressure = db.reference("Pressure").get()
    Rain_Value = db.reference("Rain_Value").get()
    Smoke = db.reference("Smoke").get()
    Temperature = db.reference("Temperature").get()

    def main():
       (Air_Quality,Altitude,Cng,Humidity,Ldr,Lpg,Pressure,Rain_Value,Smoke,Temperature)
    data = {}
    data = {

        "Air_Quality":Air_Quality, 
        "Altitude":Altitude,
        "Cng":Cng, 
        "Humidity":Humidity,
        "Ldr":Ldr, 
        "Lpg":Lpg,
        "Pressure":Pressure, 
        "Rain_Value":Rain_Value,
        "Smoke":Smoke, 
        "Temperature":Temperature
        
    }
    New_Data = str(json.dumps(data))
    main()
    with open("data.json", "w") as file:
       file.write(f"[{New_Data}]")
       file.write("\n") 
       json_dump = data
       return json_dump

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port= PORT)
