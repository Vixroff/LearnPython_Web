from flask import Flask, render_template
from webapp.model import db, News
from webapp.get_weather import weather_by_city


def create_app(): 
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)


    @app.route('/')
    def index():
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        title = 'Новости Python'
        news_list = News.query.order_by(News.published .desc()).all()
        #Возвращаем на выход HTML страничку:
        return render_template('index_1.html', page_title = title, weather = weather, news_list = news_list)

    return app