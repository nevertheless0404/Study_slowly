# https://www.acmicpc.net/problem/2669


import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.12/직사각형 네개의 합집합의 면적 구하기.txt")

# 모든 좌표는 1 이상 100 이하이기 때문에 !
drawing = [[0] * 100 for _ in range(101)]

# 네개의 직사각형의 반복문
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    # 행열 모아주기
    for i in range(x1, x2):
        for j in range(y1, y2):
            drawing[i][j] = 1
count = 0
for k in drawing:
    count += sum(k)

print(count)

