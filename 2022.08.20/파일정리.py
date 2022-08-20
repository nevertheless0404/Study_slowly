# https://www.acmicpc.net/problem/20291

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.20/파일정리.txt")

n = int(input())
file = {}

for i in range(n):
    a = input().split('.')[1]
    if a in file:
        file[a] += 1
    else:
        file[a] = 1

result = list(file.keys())
result.sort()

for j in result:
    print(j, file[j])