import copy
T = int(input())
for t in range(1, T + 1):
    word_list = list(input())
    word_list2 = copy.deepcopy(word_list)
    len_w = len(word_list)
    for i in range(len_w // 2):
        word_list[i], word_list[len_w - 1 - i] = word_list[len_w - 1 - i], word_list[i]
    if word_list == word_list2:
        print('#{0} 1'.format(t))
    else:
        print('#{0} 0'.format(t))