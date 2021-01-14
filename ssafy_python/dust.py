# pip install requests bs4 lxml
import requests
from bs4 import BeautifulSoup

key = 'EZNDtyh1IjgPkd8AhJtHhY7xMSWJLW0kSAFkJbBBLz5319e2mL6qJCogpnmiToDgij9Q1S0W%2Fyt9RvifciKbtQ%3D%3D'
url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={key}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'

response = requests.get(url).text
data = BeautifulSoup(response, 'xml')
item = data('item')[5]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)
if(dust>150):
    print("현재 지수는 "+str(dust)+"으로 매우나쁨 단계입니다.")
elif(dust<=150 and dust>80):
    print("현재 지수는 "+str(dust)+"으로 나쁨 단계입니다.")
elif(dust<=80 and dust>30):
    print("현재 지수는 "+str(dust)+"으로 보통 단계입니다.")
else :print("현재 지수는 "+str(dust)+"으로 좋음 단계입니다.")