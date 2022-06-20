from flask import Blueprint, current_app, render_template
from webapp.get_weather import weather_by_city
from webapp.news.models import News

blueprint = Blueprint('news', __name__, )

@blueprint.route('/')
def index():
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    title = 'Новости Python'
    news_list = News.query.order_by(News.published .desc()).all()
    #Возвращаем на выход HTML страничку:
    return render_template('news/index.html', page_title = title, weather = weather, news_list = news_list) 