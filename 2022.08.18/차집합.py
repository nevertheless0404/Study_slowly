# https://www.acmicpc.net/problem/1822

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.18/차집합.txt")

na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a-b))
print(*sorted(list(a-b)))