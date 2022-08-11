# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.11/홀수만 더하기.txt")

t = int(input())
for tc in range(1, t+1):
    n = list(map(int, input().split()))
    count = 0
    for i in range(len(n)):
        if n[i] %2 == 1:
            count += n[i]
    print('#%d %d' % (tc, count))
