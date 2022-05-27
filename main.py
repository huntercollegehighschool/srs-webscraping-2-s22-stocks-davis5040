import bs4
import requests
from bs4 import BeautifulSoup
import time
#import matplotlib.pyplot as plt


def parsePrice(STOCK_NAME):
    r = requests.get('https://www.marketwatch.com/investing/stock/'+STOCK_NAME+'?mod=search_symbol') #returns html of the website
    #print("r", r.text)
    soup = BeautifulSoup(r.text, 'html.parser') #use beautiful soup to parse the html; lxml
    #print("soup:", soup.title.text)
    price = soup.find('div',{'class':'intraday__data'}).find_all('bg-quote')[0].text
    return price

price = parsePrice("amzn").replace(",", '')
print(price)