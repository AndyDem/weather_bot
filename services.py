import requests
from datetime import datetime
from config import OPEN_WEATHER_TOKEN


def get_weather(city):
    try:
        raw_weather_data = get_raw_weather(city)
        current_weather = get_message(raw_weather_data)
        return current_weather

    except Exception as e:
        print(e)
        return 'Something happened, check the city or try again, please'

def get_raw_weather(city):
    r = requests.get(
        f'https://api.openweathermap.org/raw_weather_data/2.5/weather?q={city}&appid={OPEN_WEATHER_TOKEN}&units=metric'
    )
    return r.json()

def get_message(raw_weather_data):
    city = raw_weather_data['name']
    today = datetime.fromtimestamp(raw_weather_data['dt']).date().strftime('%d-%m-%Y')
    current_temperature = int(raw_weather_data['main']['temp'])
    current_feels_like = int(raw_weather_data['main']['feels_like'])
    current_humidity = raw_weather_data['main']['humidity']
    current_wind_speed = raw_weather_data['wind']['speed']
    today_sunrise = datetime.fromtimestamp(
        raw_weather_data['sys']['sunrise'])
    today_sunset = datetime.fromtimestamp(
        raw_weather_data['sys']['sunset'])
    today_daylength = today_sunset - today_sunrise
    current_weather = raw_weather_data['weather'][0]['description'].capitalize()

    current_weather = add_emoji(current_weather)

    message = f'Current weather in {city} for today {today} is:\n' \
        f'{current_weather}\n' \
        f'Temperature: {current_temperature}°C, feels like {current_feels_like}°C\n' \
        f'Humidity: {current_humidity}%\n' \
        f'Wind speed: {current_wind_speed} m/s\n' \
        f'Sunrise time: {today_sunrise.time()}\n' \
        f'Sunset time: {today_sunset.time()}\n' \
        f'Day length is {today_daylength}'

    return message

def add_emoji(text:str):
    emoji = {
        "Clear": " \U00002600",
        "Clouds": " \U00002601",
        "Rain": " \U00002614",
        "Drizzle": " \U00002614",
        "Thunderstorm": " \U000026A1",
        "Snow": " \U0001F328",
        "Mist": " \U0001F32B"
    }

    for word in text.split():
            if word in emoji:
                text += emoji[word]
                break

    return text


def main():
    city = input('City: ')
    print(get_weather(city))


if __name__ == '__main__':
    main()
