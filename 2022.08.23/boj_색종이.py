# https://www.acmicpc.net/problem/10163

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.23/boj_색종이.txt")

N = int(input())
board = [[0] * 1001 for _ in range(1001)]
data = [] # 모든 사각형의 정보를 담아둘 리스트

# 색종이 위치 시키기
for n in range(N):
    Y, X, W, H = map(int, input().split())
    data.append((Y, X, W, H)) # 일단 담아둘 것

    for x in range(W):
        for y in range(H):
            board[Y + y][X + x] += 1
# print(data)

# 맨 마지막에 위치시킨 색종이부터 면적 세기
# 출력은 처음 값부터 해야하므로 잠시 담아둘 변수 필요
result = []
for n in range(N):
    Y, X, W, H = data.pop()
    area = 0
    # print(X, Y, W, H)

    for x in range(W):
        for y in range(H):
            if board[Y + y][X + x] > 0: # 면적확인
                area += 1
                board[Y + y][X + x] = 0 # 초기화
    result.append(area)

for _ in range(len(result)):
    print(result.pop())
