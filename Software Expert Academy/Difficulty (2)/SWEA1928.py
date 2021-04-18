'''
swea1928. Base64 Decoder (D2)
'''
from base64 import b64decode

t = int(input())
for t in range(1, t+1):
    print(f'#{t} {b64decode(input()).decode("UTF-8")}')
