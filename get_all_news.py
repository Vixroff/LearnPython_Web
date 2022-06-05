from webapp.get_news import get_news_python
from webapp import create_app

app = create_app()
with app.app_context():
    get_news_python()