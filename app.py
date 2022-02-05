from weakref import ref
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from rsa import PrivateKey
from flask import *
import json, time
import requests

cred = credentials.Certificate('firebase-sdk.json')
app = Flask(__name__)
firebase_admin.initialize_app(cred, {

'databaseURL': 'https://weather-station-1514a-default-rtdb.firebaseio.com/'})

Air_Quality = db.reference("Air_Quality").get()
Altitude = db.reference("Altitude").get()
cng = db.reference("Cng").get()
Humidity = db.reference("Humidity").get()
Ldr = db.reference("Ldr").get()
Lpg =db.reference("Lpg").get()
Pressure =db.reference("Pressure").get()
Rain_Value =db.reference("Rain_Value").get()
Smoke = db.reference("Smoke").get()
Temperature = db.reference("Temperature").get()

print("Weather Station Data From Firebase With Time Stamp")
print("---------------------------------------------------")
print("Date & Time =" , time.asctime())
print("Air_Quality=" , Air_Quality)
print( "Altitude =",Altitude)
print("Cng =",cng)
print("Humidity =", Humidity)
print("Ldr =", Ldr)
print("Lpg =", Lpg)
print("Pressure =", Pressure)
print("Rain_Value =", Rain_Value)
print("Smoke =",Smoke)
print("Temperature =" ,Temperature)
print("\n")


@app.route('/', methods=['GET'])
def home_page():
    data_set = {"Date & Time =": time.asctime(), "Air_Quality =" : Air_Quality, "Altitude =" : Altitude,  "Cng =": cng, 
                                                 "Humidity =" : Humidity, "Ldr =" : Ldr,  "Lpg =" : Lpg, "Pressure =" : Pressure,
                                                 "Rain_Value =" : Rain_Value,  "Smoke =": Smoke, "Temperature =" : Temperature}
    json_dump = json.dumps(data_set)

    return json_dump
if __name__ == '__main__':
    app.run(port=5000)
