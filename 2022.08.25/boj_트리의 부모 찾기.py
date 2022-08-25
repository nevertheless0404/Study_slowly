# https://www.acmicpc.net/problem/11725

import sys
sys.setrecursionlimit(10 ** 9)
from turtle import st
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.25/boj_트리의 부모 찾기.txt")


n = int(input())
graph = [[] for _ in range(n+1)]
parents = [0] * (n+1)

for _ in range(n-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start):
    # 연결된 노드 모두 탐색
    for adj in graph[start]:
        # 한번도 방문 한적 없다면 
        if parents[adj] == 0:
            # 부모노드 저장 
            parents[adj] = start    
            dfs(adj)
dfs(1)

for i in range(2, n+1):
    print(parents[i])