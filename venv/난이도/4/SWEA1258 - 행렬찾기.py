'''
SWEA1258 - 행렬찾기 (D4)
'''
T = int(input())

# def search_size(r,c):
#     r_cnt = 0
#     c_cnt = 0
#
#     # 행 길이
#     for i in range(r, N):
#         if arr[i][c] != 0:
#             r_cnt += 1
#         else:
#             break
#
#     # 열 길이
#     for i in range(c, N):
#         if arr[r][i] != 0:
#             c_cnt += 1
#         else:
#             break
#
#     ans.append([r_cnt, c_cnt, r_cnt * c_cnt])
#     init(r, c, r_cnt, c_cnt)
#
# # 빈용기로 초기화
# def init(r,c,r_cnt,c_cnt):
#     for i in range(r, r + r_cnt):
#         for j in range(c, c + c_cnt):
#             arr[i][j] = 0
#
# def counting_sort(idx):
#     cnt = [0] * 10001
#     sort_ans = [0] * len(ans)
#
#     # 카운팅
#     for i in range(len(ans)):
#         cnt[ans[i][idx]] += 1
#
#     # 누적
#     for i in range(1, len(cnt)):
#         cnt[i] += cnt[i-1]
#
#     # 정렬하여 넣는 과정
#     for i in range(len(ans)-1, -1, -1):
#         sort_ans[cnt[ans[i][idx]]-1] = ans[i]
#         cnt[ans[i][idx]] -= 1
#
#     return sort_ans


for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                r, c = i, j
                #범위를 앞에 위치
                while r < N and arr[r][j] != 0:
                    r += 1
                while c < N and arr[i][c] != 0:
                    c += 1
                ans.append([r-i, c-j])

                #초기화 작업
                for a in range(i, r):
                    for b in range(j, c):
                        arr[a][b] = 0
    ans.sort(key = lambda x: (x[0] * x[1], x[0]))

    print("#{} {}".format(t, len(ans)), end=" ")
    for i in range(len(ans)):
        print("{} {}".format(ans[i][0], ans[i][1]), end=" ")
    print()

    # for t in range(1, T + 1):
    #     N = int(input())
    #     arr = [list(map(int, input().split())) for _ in range(N)]
    #     ans = []
    #
    #     for i in range(N):
    #         for j in range(N):
    #             if arr[i][j] != 0:
    #                 search_size(i, j)
    #
    #     ans = counting_sort(0)  # 행 기준 정렬
    #     ans = counting_sort(2)  # 행렬 크기 정렬
    #
    #     print('#{} {}'.format(t, len(ans)), end=" ")
    #     for i in range(len(ans)):
    #         print('{} {}'.format(ans[i][0], ans[i][1], end=" "))
    #     print()