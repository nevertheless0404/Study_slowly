# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.28/sw_min max.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    ai = list(map(int, input().split()))

    print('#{} {}'.format(tc, max(ai)-min(ai)))

