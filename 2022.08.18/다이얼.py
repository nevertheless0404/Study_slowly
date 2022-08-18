# https://www.acmicpc.net/problem/5622

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.18/다이얼.txt")

num = {
    1:' ', 2:'ABC', 3:'DEF', 4:'GHI', 5:'JKL', 6:'MNO', 7:'PQRS', 8:'TUV', 9:'WXYZ', 0:' '
}

word = input()
cnt = 0
for i in word:
    for j in range(0, 10):
        if i in num[j]:
            cnt += j + 1
            break
print(cnt)