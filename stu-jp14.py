import requests
from bs4 import BeautifulSoup

def trade_spider():
    url = 'http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a', {'class':'span'}):
        href = link.get('href')
        print(href)
        print(title)

trade_spider()
