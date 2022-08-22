# https://ywtechit.tistory.com/70

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.22/그림.txt")
from collections import deque

def bfs(x,y):
    cnt = 1
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True 

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True 
                    queue.append((nx,ny))
                    cnt += 1
    return cnt

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n_cnt, max_cnt = 0,0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            n_cnt += 1
            max_cnt = max(max_cnt, bfs(i,j))

print(n_cnt)
print(max_cnt)