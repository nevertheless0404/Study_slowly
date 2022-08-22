# https://www.acmicpc.net/problem/2644

from importlib.resources import contents
import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.22/촌수계산.txt")

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start, cnt):
    cnt += 1
    visited[start] = True 

    if start == b:
        result.append(cnt)

    for adj in graph[start]:
        if not visited[adj]:
            dfs(adj, cnt)
    
dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1) 