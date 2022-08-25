# https://www.acmicpc.net/problem/11720

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.25/boj_숫자의 합.txt")

n = int(input())
m = list(input())
total = 0

for i in m:
    total += int(i)
print(total)
