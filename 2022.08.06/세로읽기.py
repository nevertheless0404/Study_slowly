# https://www.acmicpc.net/problem/10798

import sys
sys.stdin = open("/Users/yuyeong/Desktop/1일 1코딩/2022.08.06/세로읽기.txt")

# 5행 15열 리스트 형태 선언
data = [[0]*15 for i in range(5)]

for i in range(5):
    s = list(input())
    for j in range(len(s)):
        data[i][j] = s[j]

for i in range(15):
    for j in range(5):
        if data[j][i] != 0:
            print(data[j][i],end='')
        else:
            continue