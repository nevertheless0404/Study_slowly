# https://www.acmicpc.net/problem/10546


import sys
sys.stdin = open("/Users/yuyeong/Desktop/1일 1코딩/2022.08.02/배부른 마라토너.txt")

names = {}

n = int(input())
for _ in range(n):
    name = input() # 참가자 이름 넣기
    if name in names:   # 딕셔너리에 이미 존재하면
        names[name] += 1
    else:
        names[name] = 1    # 존재하지 않으면 1 넣기
    
for _ in range(n-1):
    name = input()
    names[name] -=1   # 완주한 사람의 이름을 넣어주고 빼준다.

for key in names:
    if names[key] > 0:    # 값에 0 그러니까 존재하지 않는 값을 찾는다.

        print(key)     # 그때 그 값을 반환!! 완주하지 못한 사람 
