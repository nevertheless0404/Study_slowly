# https://www.acmicpc.net/problem/2846

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.19/오르막.txt")

n = int(input())
m = list(map(int, input().split()))

tmp = 0
max_m = 0

for i in range(1, n):
    slope = m[i] - m[i-1]
    if slope >= 1:
        # 경사차이 누적
        tmp += slope
    else:
        tmp = 0

tmp > max_m 
max_m = tmp

print(max_m)