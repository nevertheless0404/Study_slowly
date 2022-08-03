# https://www.acmicpc.net/problem/2711

import sys
sys.stdin = open("/Users/yuyeong/Desktop/1일 1코딩/2022.08.03/오타맨 고창영.txt")

t = int(input())
for tc in range(t):
    n, word = input().split()
    n = int(n)
    print(word[:n-1]+word[n:])