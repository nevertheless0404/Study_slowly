# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjMgaALgDFAUq

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.16/가랏!RC카.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    speed = 0
    distance = 0
    for _ in range(n):
        command = list(map(int, input().split()))
        # 첫요소가 가속일 경우 두번쨰 요소를 누적
        if command[0] == 1:
            speed += command[1]
            # 감속일 경우 현재 속도 값이 두 번쨰 요소보다 클 경우 해당 값만큼 감소 
        elif command[0] == 2:
            if speed > command[1]:
                speed -= command[1]
            else:
                speed = 0
        distance += speed
    
    print('#%d %d' % (tc, distance))
            