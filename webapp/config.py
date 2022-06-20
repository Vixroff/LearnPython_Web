from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
WEATHER_DEFAULT_CITY = "Saint-Petersburg, Russia"
WEATHER_API_KEY = "572d3a1105404fe4837141956222705"
SECRET_KEY = 'FRFRFRFRFRFRF'
REMEMBER_COOKIE_DURATION = timedelta(days=5)
