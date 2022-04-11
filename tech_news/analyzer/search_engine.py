from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    result = search_news({"title": {"$regex": title, "$options": 'i'}})
    final_result = []
    for news in result:
        final_result.append((news["title"], news["url"]))
    return final_result


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        result = search_news({"timestamp": {"$regex": date, "$options": 'i'}})
        final_result = []
        for news in result:
            final_result.append((news["title"], news["url"]))
        return final_result
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
