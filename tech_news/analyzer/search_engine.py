from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    result = search_news({"title": {"$regex": title, "$options": 'i'}})
    final_result = []
    for news in result:
        final_result.append((news["title"], news["url"]))
    return final_result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
