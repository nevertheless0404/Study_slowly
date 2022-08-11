# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QQhbqA4QDFAUq

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.11/최대수 구하기.txt")

t = int(input())
for i in range(1, t+1):
    n = map(int, input().split())
    print(f'#{i} {max(n)}')
