import time
from flask import Flask, jsonify
from firebase_admin import credentials, db, initialize_app

app = Flask(__name__)
cred = credentials.Certificate("firebase-sdk.json")
initialize_app(
    cred, {
        "databaseURL":
        "https://weather-station-91122-default-rtdb.firebaseio.com/"
    })


@app.route('/', methods=['GET'])
def home_page():
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
    timestamp = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
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
        'timestamp': timestamp}
    return jsonify({"status": 200, "result": data_set})


@app.errorhandler(404)
def invalid_route(e):
    return jsonify({"status": 404, "result": ""})


def main():
    app.run(debug=True, host='0.0.0.0')


if __name__ == '__main__':
    main()
