# https://www.acmicpc.net/problem/17249

import sys
sys.stdin = open("/Users/yuyeong/Desktop/1일 1코딩/2022.08.03/태보태보 총난타.txt")

a,b = input().split("(^0^)")
print(a.count('@'),b.count("@"))