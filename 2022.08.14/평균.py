# https://www.acmicpc.net/problem/1546

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.14/평균.txt")

n = int(input())
score= list(map(int, input().split()))
max_s = max(score)

result = []
for i in score:
    result.append(i/max_s * 100)

print(sum(result)/n)
