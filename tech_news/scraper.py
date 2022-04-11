import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3.05)
        time.sleep(1)
        response.raise_for_status()
        return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    links = selector.css(
        ".tec--list__item .tec--card__title__link::attr(href)"
    ).getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(
        ".tec--list--lg .tec--btn::attr(href)"
    ).get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("head link[rel='canonical']::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    writer = selector.css(".z--font-bold *::text").get()
    shares_count = selector.css(
        ".tec--toolbar__item::text"
    ).get()
    comments_count = int(selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get())
    summary = selector.css(
        ".tec--article__body > p:first_child *::text"
    ).getall()
    summary = "".join(summary)
    sources = selector.css(
        ".tec--badge[rel='noopener nofollow']::text"
    ).getall()
    categories = selector.css("#js-categories a::text").getall()
    sources = [item.strip() for item in sources]
    categories = [item.strip() for item in categories]
    if writer:
        writer = writer.strip()
    else:
        writer = None
    if type(shares_count) is str:
        shares_count = int(shares_count.split(" ")[1])
    else:
        shares_count = 0
    return {"url": url, "title": title, "timestamp": timestamp,
            "writer": writer, "shares_count": shares_count,
            "comments_count": comments_count, "summary": summary,
            "sources": sources, "categories": categories}


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    result = []
    while len(result) < amount:
        html_content = fetch(url)
        links = scrape_novidades(html_content)
        for link in links:
            if len(result) <= amount:
                news = fetch(link)
                data = scrape_noticia(news)
                result.append(data)
        next = scrape_next_page_link(html_content)
        amount -= 1
        url = next
    create_news(result)
    return result
