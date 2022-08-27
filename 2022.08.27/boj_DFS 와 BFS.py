# https://www.acmicpc.net/problem/1260

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.27/boj_DFS 와 BFS.txt")

from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(start):
    visited[start] = True  # 해당 값 방문 처리 
    print(start, end=' ')
    for adj in graph[start]:
        if not visited[adj]:
            dfs(adj) # 해당 값으로 dfs돌기, 더 깊이 탐색 

def bfs(s):
    queue = deque([s])
    visited[s] = True # 해당 값을 방문처리
    while queue: # 빌 때까지 돌기
        cur = queue.popleft() # 첫번째 값을 꺼내기 
        print(cur, end=' ') # 해당 값 출력 
        for adj in graph[cur]:
            if not visited[adj]: # 방문하지 않았고 연결되어 있다면 
                queue.append(adj) # 값을 추가 
                visited[adj] = True # 방문처리 

dfs(v)

print()
visited = [False] * (n+1)

bfs(v)