from datetime import datetime
import pytz

def get_time(city: str) -> str:
    if not city:
        return "Please provide a city name."

    city = city.strip().lower()

    city_timezones = {
        "lahore": "Asia/Karachi",
        "karachi": "Asia/Karachi",
        "islamabad": "Asia/Karachi",
        "peshawar": "Asia/Karachi",
        "new york": "America/New_York",
        "london": "Europe/London",
        "tokyo": "Asia/Tokyo"
    }

    if city not in city_timezones:
        return f"City '{city}' not supported."

    tz = pytz.timezone(city_timezones[city])
    current_time = datetime.now(tz)

    return f"Current time in {city.title()} is {current_time.strftime('%Y-%m-%d %H:%M:%S')}"

