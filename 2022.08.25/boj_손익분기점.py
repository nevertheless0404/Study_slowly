# https://www.acmicpc.net/problem/1712

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.25/boj_손익분기점.txt")

a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print((a//(c-b))+1)