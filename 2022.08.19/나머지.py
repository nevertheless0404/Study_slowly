# https://www.acmicpc.net/problem/3052

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.19/나머지.txt")

n = []
for i in range(10):
    m = int(input())
    b = m % 42
    n.append(b)

s = set(n)
print(len(s))
