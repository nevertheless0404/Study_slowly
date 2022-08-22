# https://www.acmicpc.net/problem/2606

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.21/바이러스.txt")

# 컴퓨터 수 
n = int(input())
# 네트워크 상에서 직접 연결되어있는 컴퓨터 쌍의 수 
m = int(input())
# 인덱스 시작을 1로 해서 +1
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1) 
total = 0

# 인접 리스트 만들기 
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start):
    stack = [start]
    visited[start] = True 

    while stack:
        cur = stack.pop()
        if not visited[cur]:
            visited[cur] = True
        
        for adj in graph[cur]:
            if not visited[adj]:
                stack.append(adj)
# 1번 정점에서 시작
dfs(1)
print(sum(visited)-1)