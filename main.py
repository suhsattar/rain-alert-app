import requests
import os
from twilio.rest import Client


api_key = "YOUR API KEY"
account_sid = "YOUR ACCOUNT SID"
auth_token = "YOUR AUTH TOKEN"

parameters = {
    "lat": 17.385044,
    "lon": 78.486671,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☔️",
        from_='YOUR TWILIO NUMBER',
        to='YOUR VERIFIED NUMBER'
    )

    print(message.status)