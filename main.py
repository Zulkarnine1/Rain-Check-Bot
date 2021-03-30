import requests as req
from twilio.rest import Client
import os
from env import OWM_API, AUTH_TOKEN_TWILIO, ACCOUNT_SID_TWILIO

API_KEY = OWM_API
account_sid = ACCOUNT_SID_TWILIO
auth_token = AUTH_TOKEN_TWILIO

# LAT = 23.810331
# LNG = 90.412521
LAT = 26.074478
LNG = 119.296478



params = {
    "lat":LAT,
    "lon":LNG,
    "exclude":"current,daily",
    "appid":API_KEY
}

response = req.get(url="https://api.openweathermap.org/data/2.5/onecall",params=params)
response.raise_for_status()
data = response.json()["hourly"]

data = data[0:12]


will_rain = False
for item in data:
    if item["weather"][0]["id"] < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, don't forget to bring your umbrella ☔",
        from_='',
        to=''
    )

    print(message.status)
