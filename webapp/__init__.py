from flask import Flask, render_template
from webapp.get_weather import weather_by_city
from webapp.get_news import get_news_python 

def create_app(): 
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        title = 'Новости Python'
        news_list = get_news_python()
        #Возвращаем на выход HTML страничку:
        return render_template('index_1.html', page_title = title, weather = weather, news_list = news_list)

    return app