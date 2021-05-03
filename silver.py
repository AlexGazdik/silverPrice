from bs4 import BeautifulSoup as soup
import requests
from urllib.request import urlopen as uReq


my_url='https://www.kitco.com/charts/livesilver.html'
uClient = uReq(my_url)
pagehtml = uClient.read()
uClient.close
page_soup = soup(pagehtml, 'lxml')
match = page_soup.find('div', class_='data-blk bid').text
price = match[:-3]
print(price)
