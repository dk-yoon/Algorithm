'''
SWEA5185 - 이진수 (D2)
'''

T = int(input())
for t in range(1, T + 1):
    word = list(input().split())
    ten_word = int(word[1],16)
    bin_word = bin(ten_word)

    if len(bin_word[2:]) < int(word[0]) * 4:
        print(f'#{t} {"0" + bin_word[2:]}')
    else:
        print(f'#{t} {bin_word[2:]}')
