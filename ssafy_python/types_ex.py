# ctrl +b 탐색기 창 열고닫기
# 숫자 문자 boolean
number = 3
string = '문자열'
boolean = True  # 주석은 보통 2칸 띄우고 작성

print(type(number))  # alt + shift + 위아래 화살표 위아래줄 복사
print(type(string))
print(type(boolean))

string_number = '3' 
# print(string_number+5)
print(int(string_number)+5)
print(string_number+str(5))

# f-string / string interpolation
name = '윤덕영'
name2 = '김민철'
print(f'안녕하세요 저는 name입니다')
print(f'안녕하세요 저는 {name}입니다')

# 리스트
my_list = ['java', 'python']
print(my_list[0])
my_list[0] = 'javascript'  # 재 할당 가능!
print(my_list[0])
print(len(my_list))  # 리스트의 길이 구하기

# dictionary
my_home = {
    'location' : '대전',  # key: value
    'area-code' : '042',  # trailing comma : 뒤에 요소가 없어도 콤마를 붙여도 괜찮음, 추후 수정을 위해 오히려 권장함.
}
print(my_home)
print(my_home['location'])
# print(my_home['name'])  # 없는 키에 접근할 경우 key 에러 발생.
print(my_home.get('location'))
print(my_home.get('name'))  # get 방식은 키가 없을 경우 에러가 아닌 none값 반환.
# None(Null) - 아무 것도 없다는 것을 나타내는 값

# 자신의 이름, 나이, 인삿말로 구성된 my_info 딕셔너리 만들기
# 내 나이만 출력해보기
my_info = {
    '이름' : '윤덕영',
    '나이' : 27,
    '인삿말' : '안녕하세요',}
# 컨트롤 엔터를 누르면 줄만 이동하는게 가능
print(my_info['나이'])


# 실습!
coin = {
    "BTC": {
        "opening_price": "44405000",
        "closing_price": "38806000",
        "min_price": "36640000",
        "max_price": "44999000",
        "prev_closing_price": "44404000",
        "fluctate_24H": "-7463000",
        "fluctate_rate_24H": "-16.13"
    },
    "ETH": {
        "opening_price": "1458000",
        "closing_price": "1229000",
        "min_price": "1100000",
        "max_price": "1490000",
        "prev_closing_price": "1458000",
        "fluctate_24H": "-275000",
        "fluctate_rate_24H": "-18.28"
    },
    "XRP": {
        "opening_price": "364",
        "closing_price": "311.9",
        "min_price": "284.2",
        "max_price": "372.7",
        "prev_closing_price": "364.2",
        "fluctate_24H": "-90.6",
        "fluctate_rate_24H": "-22.51"
    }
}

#  1. 코인의 정보에서 BTC의 최대 가격을 출력하세요
#  2. BTC의 시가(opening price)와 XRP의 시가를 더한 결과를 출력하세요
total = int(coin['BTC']['opening_price'])+int(coin['XRP']['opening_price'])
print(coin['BTC']['max_price'])
print(total)

#실습
movie = {
    'movieInfo': {
        'movieNm': '광해, 왕이 된 남자',
        'movieNmEn': 'Masquerade',
        'showTm': '131',
        'prdtYear': '2012',
        'openDt': '20120913',
        'typeNm': '장편',
        'nations': [
            {
            'nationNm': '한국'
            }
        ],
        'genres': [
            {
            'genreNm': '사극'
            },
            {
            'genreNm': '드라마'
            }
        ],
        'directors': [
            {
            'peopleNm': '추창민',
            'peopleNmEn': 'CHOO Chang-min'
            }
        ],
        'actors': [
            {
            'peopleNm': '이병헌',
            'peopleNmEn': 'LEE Byung-hun',
            'cast': '광해/하선'
            },
            {
            'peopleNm': '류승룡',
            'peopleNmEn': 'RYU Seung-ryong',
            'cast': '허균'
            },
            {
            'peopleNm': '한효주',
            'peopleNmEn': 'HAN Hyo-joo',
            'cast': '중전'
            }
        ]
    }
}

#  1. 영화의 제목을 출력하세요
print(movie['movieInfo']['movieNm'])

#  2. 감독의 영어 이름을 출력하세요
print(movie['movieInfo']['directors'][0]['peopleNmEn'])
#  3. 이 영화의 배우가 몇 명인지 출력하세요
print(len(movie['movieInfo']['actors']))
#  api 키 발급!