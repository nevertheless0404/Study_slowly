# https://www.acmicpc.net/problem/10158

from distutils.spawn import spawn
import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.24/boj_개미.txt")

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# 증가인지 감소인지 확인하기
a = (p + t) // w
b = (q + t) // h

# 증가하는 부분 확인
if a % 2 == 0:
    x = (p + t) % w
else:
    # 감소하는 부분 확인
    x = w - (p + t) % w

if b % 2 == 0:
    y = (q + t) % h 
else:
    y = h - (q + t) % h
    
print(x, y)
