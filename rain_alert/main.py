import requests
from twilio.rest import Client
api_key = "858c12600d0f86ac5eb4eacfb9c09e80"
parameter = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
}
account_sid = "AC0f269cd530b3b0d1c5dfdd61516b7340"
auth_token = "dc7f7ddf4d0c79379cc266d9807a0c64"
will_rain: bool
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameter)
response.raise_for_status()
data = response.json()["weather"][0]["id"]
if int(data) < 700:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="its going to rain",
        from_= "+15105925987",
        to= "+2348166545589"
    )
print(message.status)
