# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjKXKALcDFAUq

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.09/1대1가위바위보.txt")

a, b = map(int, input().split())
if a > b:
    print("A")
else:
    print("B")