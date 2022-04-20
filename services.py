import requests
from datetime import datetime
from config import OPEN_WEATHER_TOKEN


def get_weather(city):

    code_to_smile = {
        "Clear": "\U00002600",
        "Clouds": "\U00002601",
        "Rain": "\U00002614",
        "Drizzle": "\U00002614",
        "Thunderstorm": "\U000026A1",
        "Snow": "\U0001F328",
        "Mist": "\U0001F32B"
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER_TOKEN}&units=metric'
        )
        data = r.json()

        city = data['name']
        today = datetime.fromtimestamp(data['dt']).date().strftime('%d-%m-%Y')
        current_temperature = data['main']['temp']
        current_feels_like = data['main']['feels_like']
        current_humidity = data['main']['humidity']
        current_wind_speed = data['wind']['speed']
        today_sunrise = datetime.fromtimestamp(
            data['sys']['sunrise'])
        today_sunset = datetime.fromtimestamp(
            data['sys']['sunset'])
        today_daylength = today_sunset - today_sunrise
        current_weather = data['weather'][0]['main']
        if current_weather in code_to_smile:
            current_weather += code_to_smile[current_weather]

        current_weather = f'Weather in {city} for today {today} is:\n' \
            f'{current_weather}\n' \
            f'Current temparature: {current_temperature}°C, which feels like {current_feels_like} °C\n' \
            f'Current humidity: {current_humidity}%\n' \
            f'Current wind speed: {current_wind_speed} m/s\n' \
            f'Sunrise time: {today_sunrise.time()}\n' \
            f'Sunset time: {today_sunset.time()}\n' \
            f'Day length is {today_daylength}'

        return current_weather

    except Exception as e:
        print(e)
        return 'Something happened, check the city or try again, please'


def main():
    city = input('City: ')
    get_weather(city)


if __name__ == '__main__':
    main()
