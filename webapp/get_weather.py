#делаем запрос на сайт прогноза погоды с помощью api_key и библиотеки requests
from flask import current_app
import requests 

def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        "key": current_app.config['WEATHER_API_KEY'],
        "q": city_name,
        "format": 'json',
        "num_of_days": 1,
        "lang": 'ru',
    }
    try:
        #запрос на сервер
        result = requests.get(weather_url, params = params)
        #проверка и возврат исключения в случае ошибки сервера 4** или 5**
        result.raise_for_status
        #ответ с сервера и обработка
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    #отработка ошибок подключения к сети и неверно введенных данных.
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return False
