# Weather Station API

## Introduction

The project provides a simple weather data as API.

## Features

The API provides the following data:-

1. Air Quality Index (AQI)
2. Altitude
3. CNG
4. Humidity
5. LDR
6. LPG
7. Pressure
8. Rain Intensity
9. Smoke
10. Temperature
11. Timestamp

## Software Stack

1. Programming language - Python
2. Database - Google Firebase
3. Containerisation - Docker
4. Currently hosted in - [Heroku](https://firebase-data-api.herokuapp.com/)

## Prereuisites

The following tools needs to be installed for development:-

1. Python
2. Docker
3. VSCode

## Instruction

1. Clone the repository.
2. cd into the repository.
3. Run the following command to build the docker file.

   ```bash
   docker build -t weather-station-api:1.0.0 `pwd`
   ```

4. Run the built docker image with the following command:-

   ```bash
   docker run -d -p 80:5000 weather-station-api:1.0.0
   ```

5. Visit the URL localhost/ in the browser to view the data.

## Contributors

1. Sreeram A J <sreeramzeno@gmail.com>
2. Sashwat K <sashwat0001@gmail.com>
