#후보군에 포함되어야 할 메뉴가 김밥, 귤, 칼국수, 마라탕
import random

lunch = ['김밥', "귤", "칼국수", "마라탕"]
restaurant = {'김밥':'042-001-0001',
    '귤':'042-002-0002',
    '칼국수':'042-003-0003',
    '마라탕':'042-004-0004'}
# print(lunch)  
print(random.choice(lunch))
print(restaurant)  

#  랜덤으로 고른 메뉴의 전화번호를 출력해주세요
menu = random.choice(lunch)
print(menu)
print(restaurant[menu])