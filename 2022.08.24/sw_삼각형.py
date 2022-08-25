# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE&problemTitle=2005&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.24/sw_삼각형.txt")

t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    board = [[0] * n for _ in range(n)]
    for i in range(n) :
        board[i][0] = 1

    for i in range(1, n) :
        for j in range(1, n) :
            # 1번째 행, 1번째 열부터 해당 인덱스의 값을 왼쪽 대각선 위
            board[i][j] = board[i-1][j-1] + board[i-1][j]

    print('#%d' % tc)
    for i in range(n) :
        for j in range(n) :
            if board[i][j] != 0 :
                print(board[i][j], end=' ')
        print()