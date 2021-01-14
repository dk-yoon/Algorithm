import requests
from bs4 import BeautifulSoup

url = 'http://finance.naver.com/sise/'
response = requests.get(url).text
soup = BeautifulSoup(response,'html.parser')
kospi = soup.select_one('#KOSPI_now')
result = kospi.text
print(result)