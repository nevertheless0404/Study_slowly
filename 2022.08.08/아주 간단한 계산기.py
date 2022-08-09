# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjsYKAMIDFAUq

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.08/아주 간단한 계산기.txt")

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
