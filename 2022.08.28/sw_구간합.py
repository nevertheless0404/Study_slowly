# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

from distutils.spawn import spawn
import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.28/sw_구간합.txt")

t =int(input())

for tc in range(1,t+1):
    n, m=map(int,input().split())
    lst = list(map(int, input().split()))
    new = []

    for i in range(n-m+1):
        result=0
        for j in range(i,i+m):
            result += lst[j]
        new.append(result)

    print('#{} {}'.format(tc, max(new)-min(new)))


