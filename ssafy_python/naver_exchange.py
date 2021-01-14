import requests
from bs4 import BeautifulSoup

url = 'http://finance.naver.com/marketindex/'
response = requests.get(url).text
soup = BeautifulSoup(response,'html.parser')
exchange = soup.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value')
result = exchange.text
print(result)