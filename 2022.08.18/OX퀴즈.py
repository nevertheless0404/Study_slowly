# https://www.acmicpc.net/problem/8958

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.18/OX퀴즈.txt")

n = int(input())
for i in range(n):
    cnt = 0
    sum = 0
    quiz = list(input())

    for j in quiz:
        if j == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)
