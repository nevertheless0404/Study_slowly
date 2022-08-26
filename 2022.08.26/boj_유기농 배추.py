# https://www.acmicpc.net/problem/1012

from pydoc import visiblename
import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.26/boj_유기농 배추.txt")
from collections import deque

t = int(input())


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 노드가 1이면서 방문하지 않았다면 bfs 실행
# 해당 노드와 인접한 노드 중 1인 노드들을 방문
# 1인 노드의 주변 노드들 역시 모두 방문 처리 
def bfs (a,b):
    q = deque([])
    # 배추 위치 넣어주기
    q.append((a,b))
    visitied[a][b] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 나가지 않게!
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            
            # 아직 방문하지 않았다면
            if not visitied[nx][ny]:
                # 방문처리
                visitied[nx][ny] = True
                # 그래프에 넣기!
                if graph[nx][ny]:
                    q.append((nx,ny))


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*n for _ in range(m)]
    visitied =[[False]*n for _ in range(m)]
    
    # 다시 탐색 하다가 노드가 1이면 방문하지 않은 노드가 있으면 
     # 지렁이가 필요한 배추!
    for _ in range(k):
        a,b = map(int, input().split())
        graph[a][b] = 1
    cnt = 0
 
    for i in range(m):
        for j in range(n):
            if not visitied[i][j] and graph[i][j]:
                cnt += 1
                bfs(i,j)
    print(cnt)