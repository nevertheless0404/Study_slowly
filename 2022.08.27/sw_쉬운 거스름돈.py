# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PsIl6AXIDFAUq

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.27/sw_쉬운 거스름돈.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    n_list = [0] * 8
    for i in range(8):
        if n // money[i] != 0:
            n_list[i] = n//money[i]
            n = n%money[i]
    print('#{}'.format(tc))
    print(*n_list)
