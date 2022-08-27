# https://www.acmicpc.net/problem/18258


import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.27/boj_큐2.txt")

from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    m = input().split()
    if  m[0] == 'push':
        queue.append(int(m[1]))

    elif m[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    
    elif m[0] == 'size':
        print(len(queue))
    
    elif m[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif m[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    
    elif m[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])