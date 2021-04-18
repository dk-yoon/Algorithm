'''
연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.

해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면

”YYYY/MM/DD”형식으로 출력하고,

날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
'''


t = int(input())
thirtyone = ['01','03','05','07','08','10','12']
thirty = ['04','06','09','11']
twentyeight = ['02']
for t in range (1,t+1):
    date = str(input())
    year = (date[0:4])
    month = str(date[4:6])
    day = int(date[6:8])
    strday = str(date[6:8])
    if (month in thirtyone and day < 32):
        print(f'#{t} {year}/{month}/{strday}')
    elif (month in thirty and day < 31):
        print(f'#{t} {year}/{month}/{strday}')
    elif (month in twentyeight) and day < 29:
        print(f'#{t} {year}/{month}/{strday}')
    else:
        print(f'#{t} -1')