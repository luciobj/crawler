from tech_news.database import get_collection, search_news


# Requisito 10
def top_5_news():
    result = get_collection().aggregate([
            {"$addFields": {
                "popularidade": {"$add": [
                    "comments_count",
                    "shares_count"
                ]}}},
            {"$sort": {"popularidade": -1}},
            {"$limit": 5}])
    final_result = []
    for news in result:
        final_result.append((news["title"], news["url"]))
    return final_result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
