# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.18/새로운 불면증 치료법.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    data = [0] * 10
    cnt = 1

    while 0 in data:
        num = str(n * cnt)
        for i in range(len(num)):
            data[int(num[i])] += 1
        cnt += 1

    print('#{} {}'.format(tc, num))

            
            
