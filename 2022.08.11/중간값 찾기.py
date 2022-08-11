# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QPsXKA2UDFAUq

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.11/중간값 찾기.txt")

n = int(input())
data = list(map(int, input().split()))

data.sort()
len_value = n // 2
print(data[len_value])