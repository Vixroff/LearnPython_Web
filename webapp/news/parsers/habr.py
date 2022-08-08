import locale
import platform

from bs4 import BeautifulSoup

from datetime import datetime, timedelta 

from webapp.db import db
from webapp.news.models import News
from webapp.news.parsers.utils import get_html, save_news

if platform.system()== 'Windows':
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU')


def parse_habr_date(date_str):
    if 'сегодня' in date_str:
        today = datetime.now()
        date_str = date_str.replace('сегодня', today.strftime('%d  %B'))
    elif 'вчера' in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replace('вчера', yesterday.strftime('%d  %B'))
    try:
        return datetime.strptime(date_str, '%d  %B   в %H:%M')
    except ValueError as d:
        return datetime.now()


def get_news_snippets():
    html = get_html('https://habr.com/ru/search/?q=python&target_type=posts&order=date')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('div', class_ = "tm-articles-list").findAll('article', class_='tm-articles-list__item')
        for news in all_news:
            title = news.find('a', class_='tm-article-snippet__title-link').find('span').text
            url = 'https://habr.com' + news.find("a", class_="tm-article-snippet__title-link")['href']
            published = news.find('span', class_='tm-article-snippet__datetime-published').find('time').text
            published = parse_habr_date(published)       
            save_news(title, url, published)

def get_news_content():
    news_without_content = News.query.filter(News.text.is_(None))
    for news in news_without_content:
        html = get_html(news.url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            news_content = soup.find(id='post-content-body').decode_contents()
            if news_content:
                news.text = news_content
                db.session.add(news)
                db.session.commit()
