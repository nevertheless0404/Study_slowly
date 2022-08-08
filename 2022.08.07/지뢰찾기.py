# https://www.acmicpc.net/problem/4396

from re import search
import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.07/지뢰찾기.txt")

n = int(input())
game_board = [list(input()) for _ in range(n)]
game_open = [list(input()) for _ in range(n)]
result = []
bomb_find = False

# 좌표 설정
data_i = [1,0,-1,0,1,-1,1,-1]
data_j = [0,1,0,-1,-1,1,1,-1]

for i in range(n):
    tmp = []
    for j in range(n):
        cnt = 0
        if game_open[i][j] == 'x' and game_board[i][j] == '*':
            bomb_find = True
        if game_open[i][j] == 'x':
            for k in range(8):
                searxh_i = i + data_i[k]
                search_j = j + data_j[k]
                # 탐색_y 탐색_x의 범위는 리스트를 벗어나면 안된다.
                # 리스트의 범위는 0 ~ 7(리스트의 길이 8)
                if 0 <= searxh_i <= n-1 and 0<= search_j <= n-1:
                    if game_board[searxh_i][search_j] == '*':
                        cnt += 1
            # 지뢰수 넣기 
            tmp.append(str(cnt))
        else:
            # '.'이라면 결과에 넣기!
            tmp.append('.')
    result.append(tmp)

# 지뢰를 발견했으면 지뢰 위치를 결과보드의 표시 
if bomb_find:
   for i in range(n):
        for j in range(n):
            if game_board[i][j] == '*':
                result[i][j] = '*'

for data in result:
    print(''.join(data))


    
     

