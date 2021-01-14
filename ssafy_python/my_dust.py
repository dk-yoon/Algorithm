#  만들어진 url을 통해서 광진구의 미세먼지 농도를 화면에 출력
#  1. url 요청
#  2. json 응답을 dict로 만들고
#  3. 광진구의 미세먼지 농도가 어딨는지 파악
#  4. 출력

import requests
from bs4 import BeautifulSoup
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=ewupYf9SnigAutlyXo8O1x9BxcmhWK9JEidWvDAwA3qmwVrziHhUuTuY8Bc1KwohKjBaBYb5flVPXaTZ5xCOlg%3D%3D&returnType=json&numOfRows=5&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
response = requests.get(url).json() #2
dust = response['response']['body']['items'][0]['stationName']
print(dust)
