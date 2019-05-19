import requests
from bs4 import BeautifulSoup


def grab_ten_news():
    link = 'http://www.reuters.com/news/'
    page = requests.get(link)

    soup = BeautifulSoup(page.text, 'html.parser')

    counter = 0
    news = []
    for new in soup.find_all("h3", class_="story-title"):
        if new.string is not None and counter < 10:
            counter += 1
            news.append(new.string)
    return news
