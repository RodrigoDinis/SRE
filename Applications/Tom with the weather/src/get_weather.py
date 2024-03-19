import traceback
import requests
import json

# Local files
import logger

# Parameters
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 38.7167,
	"longitude": -9.1333,
	"hourly": ["temperature_2m", "rain"],
	"forecast_days": 1
}


def request_weather():
    try:
        get_weather = requests.get(url=url, params=params)
        return json.loads(get_weather.content)
    except Exception as e:
        log.error(f"{e} - {traceback.format_exc()}")
        return None


def calculate_statistics(weather_data):
    temperature_data = weather_data["hourly"]["temperature_2m"]
    rain_data = weather_data["hourly"]["rain"]

    # Calculate average temperature
    avg_temperature = sum(temperature_data) / len(temperature_data)

    # Calculate average rain
    avg_rain = sum(rain_data) / len(rain_data)

    # Calculate maximum temperature and rain
    max_temperature = max(temperature_data)
    max_rain = max(rain_data)

    # Calculate minimum temperature and rain
    min_temperature = min(temperature_data)
    min_rain = min(rain_data)

    return avg_temperature, avg_rain, max_temperature, min_temperature, max_rain, min_rain


def describe_weather_data(weather_data):
    try:
        calculate_statistics(weather_data)
        avg_temperature, avg_rain, max_temperature, min_temperature, max_rain, min_rain = calculate_statistics(
            weather_data)
        result = f"Weather in Lisbon - Last 24 hours"
        result += f"Average Temperature: {avg_temperature:.2f} °C\n"
        result += f"Average Rain: {avg_rain:.2f} mm\n"
        result += f"Maximum Temperature: {max_temperature:.2f} °C\n"
        result += f"Minimum Temperature: {min_temperature:.2f} °C\n"
        result += f"Maximum Rain: {max_rain:.2f} mm\n"
        result += f"Minimum Rain: {min_rain:.2f} mm\n"
        return result
    except Exception as e:
        log.error(f"{e} - {traceback.format_exc()}")
        return None


def main():
    weather_data = request_weather()
    if weather_data is not None:
        weather_description = describe_weather_data(weather_data)
    else:
        weather_description = "Sorry, we couldn't retrieve weather data for the specified location and time period. Please try again later or contact support for assistance."
    print(weather_description)


if __name__ == "__main__":
    log = logger.setup_logger()
    main()
