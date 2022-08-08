# https://www.acmicpc.net/problem/2178

from collections import deque 
import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.08/미로 탐색.txt")

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs (i, j):
    # 초기화
    queue = deque()
    # 초기화 위치 
    queue.append((i, j))

    while queue:
        # 맨 앞에 있는 수를 뺴준다. 
        i, j = queue.popleft()

        # 4방향에 대해서 이동 ! 
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            # 미로의 벽을 넘어가는지
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            # 벽에 닿는지 
            if graph[ni][nj] == 0:
                continue

            # 넘겨진 칸에 1이 써져 있다면 그 칸으로 이동 가능!
            if graph[ni][nj] == 1:
                graph[ni][nj] = graph[i][j] + 1
                # 지금 위치한 값을 전달해 위치를 옮겼다
                queue.append((ni,nj))
    
    return graph[n-1][m-1]

print(bfs(0,0))