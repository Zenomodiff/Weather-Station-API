import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask
import json, time

app = Flask(__name__)

cred = credentials.Certificate("firebase-sdk.json")
firebase_admin.initialize_app(cred,{

    'databaseURL': 'https://weather-station-91122-default-rtdb.firebaseio.com/'
})

Air_Quality = db.reference('Air_Quality')
Altitude = db.reference('Altitude')
Cng = db.reference('Cng')
Humidity = db.reference('Humidity')
Ldr = db.reference('Ldr')
Lpg = db.reference('Lpg')
Pressure = db.reference('Pressure')
Rain_Value = db.reference('Rain_Value')
Smoke = db.reference('Smoke')
Temperature = db.reference('Temperature')

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Air_Quality': Air_Quality.get(), 'Altitude': Altitude.get(), 'Cng': Cng.get(), 'Humidity': Humidity.get(), 'Ldr': Ldr.get(), 'Lpg': Lpg.get(), 'Pressure': Pressure.get(), 'Rain_Value': Rain_Value.get(), 'Smoke': Smoke.get(), 'Temperature': Temperature.get(), 'timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump
if __name__ == '__main__':
    app.run(port=5000)

