from datetime import datetime
import pytz

def get_time(city):
    city_timezones = {
        "lahore": "Asia/Karachi",
        "karachi": "Asia/Karachi",
        "peshawar": "Asia/Karachi",
        "islamabad": "Asia/Karachi",
        "new york": "America/New_York",
        "london": "Europe/London",
        "tokyo": "Asia/Tokyo"
    }

    city = city.lower()

    if city in city_timezones:
        tz = pytz.timezone(city_timezones[city])
        return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

    return "City not supported"
