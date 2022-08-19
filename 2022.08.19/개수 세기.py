# https://www.acmicpc.net/problem/10807

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.19/개수 세기.txt")

n = int(input())
num = list(map(int, input().split()))

m = int(input())
# 찾으려는 정수를 count를 통해 몇개인지 출력 
print(num.count(m))