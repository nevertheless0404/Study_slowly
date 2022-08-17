# https://www.acmicpc.net/problem/2578

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.17/빙고.txt")
input = sys.stdin.readline

# 숫자들의 위치 기록
board = dict()
check = [[0]*5 for i in range(5)]
for i in range(5):
    a = list(map(int,input().split()))
    for j in range(5):
        board[a[j]] = (i,j)

tick = 0
for _ in range(5):
    a = list(map(int,input().split()))
    for i in range(5):
        tick += 1
        
        # 불린 숫자가 보드에 있을 경우
        if a[i] in board:
            # 딕셔너리를 이용해 기록
            check[board[a[i]][0]][board[a[i]][1]] = 1
            
            # 빙고 세주기
            bingo = 0
            # 가로 세로 빙고 세주기
            for j in range(5):
                if sum(check[j]) == 5:
                    bingo+=1
                if sum([k[j] for k in check]) == 5:
                    bingo+=1
            # 대각선 빙고 세주기 
            if check[0][4]+check[1][3]+check[2][2]+check[3][1]+check[4][0] == 5:
                bingo+=1
            if check[0][0]+check[1][1]+check[2][2]+check[3][3]+check[4][4] == 5:
                bingo+=1
                
            if bingo >= 3:
                print(tick)
                sys.exit()


