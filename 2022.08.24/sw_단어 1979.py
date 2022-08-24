# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq&

from posixpath import split
import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.24/_1979.txt")

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if data[i][j] == 1:
                cnt += 1
            if data[i][j] == 0 or j == n - 1:
                if cnt == k:
                    result += 1
                if data[i][j] == 0:
                    cnt = 0
    
    for i in range(n):
        cnt = 0
        for j in range(n):
            if data[j][i] == 1:
                cnt += 1
            if data[j][i] == 0 or j == n - 1:
                if cnt == k:
                    result += 1
                if data[j][i] == 0:
                    cnt = 0

    print('#%d %d' % (tc, result))

