import requests
import datetime as dt


time_now = dt.datetime.now()
MY_LNG = 8.675277
MY_LAT = 9.081999
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response_a = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters,)
response_a.raise_for_status()
data = response_a.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
print(time_now.hour)