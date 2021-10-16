import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask
import json
import time

app = Flask(__name__)
cred = credentials.Certificate("firebase-sdk.json")
firebase_admin.initialize_app(
    cred, {
        "databaseURL":
        "https://weather-station-91122-default-rtdb.firebaseio.com/"
    })
air_quality = db.reference("Air_Quality")
altitude = db.reference("Altitude")
cng = db.reference("Cng")
humidity = db.reference("Humidity")
ldr = db.reference("Ldr")
lpg = db.reference("Lpg")
pressure = db.reference("Pressure")
rain_value = db.reference("Rain_Value")
smoke = db.reference("Smoke")
temperature = db.reference("Temperature")


@app.route('/', methods=['GET'])
def home_page():
    data_set = {
        'Air_Quality': air_quality.get(),
        'Altitude': altitude.get(),
        'Cng': cng.get(),
        'Humidity': humidity.get(),
        'Ldr': ldr.get(),
        'Lpg': lpg.get(),
        'Pressure': pressure.get(),
        'Rain_Value': rain_value.get(),
        'Smoke': smoke.get(),
        'Temperature': temperature.get(),
        'timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump


def main():
    app.run(port=5000)


if __name__ == '__main__':
    main()
