# https://www.acmicpc.net/problem/3052

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.14/나머지.txt")

n = []
for _ in range(10):
    a = int(input())
    b = a % 42
    n.append(b)
# 중복제거
s = set(n)
print(len(s))