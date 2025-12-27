import requests

def get_time(city):
    url = "https://worldtimeapi.org/api/timezone"
    response = requests.get(url).json()

    for zone in response:
        if city.lower() in zone.lower():
            data = requests.get(
                f"https://worldtimeapi.org/api/timezone/{zone}"
            ).json()
            return data["datetime"]

    return "City not found"
