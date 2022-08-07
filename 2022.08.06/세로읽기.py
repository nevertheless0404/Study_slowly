# https://www.acmicpc.net/problem/10798

import sys
sys.stdin = open("/Users/yuyeong/Desktop/1일 1코딩/2022.08.06/세로읽기.txt")

# 5행 15열 리스트 형태 선언
data = [[0]*15 for i in range(5)]

# 반복문을 통해 각 대한 열에 문자열을 입력 받는다.
for i in range(5):
    s = list(input())
    for j in range(len(s)):
        data[i][j] = s[j]

# 반복문을 통해 세로 값을 확인하고, 그 값이 0이 아닌경우 출력 
for i in range(15):
    for j in range(5):
        if data[j][i] != 0:
            print(data[j][i],end='')
        else:
            continue