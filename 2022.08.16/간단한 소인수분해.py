# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pl0Q6ANQDFAUq

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.16/간단한 소인수분해.txt")

t = int(input())
for tc in range(1, t+1):
    num = int(input())
    n = [2, 3, 5, 7, 11]
    result = [0] * 5
    for i in range(5):
        # 담겨 있는 요소를 하나식 확인 현재 num을 확인 
        # 나누어 떨어지면 num을 n로 나눈값을 갱신 
        while num % n[i] ==0:
            result[i] += 1
            num = num // n[i]
    print('#{} {}'.format(tc, ' '.join(map(str, result))))