#  로또를 만들어보세요
#  1부터 45까지의 숫자 중 6개의 무작위 숫자를 뽑습니다

import random
lotto = random.sample(range(1,46),6)
print(lotto)