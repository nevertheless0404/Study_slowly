# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PmkDKAOMDFAUq

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.23/sw_간단한 압축 풀기.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    result = ''

    for i in range(n):
        a, b = input().split()
        result += a * int(b)

    print('#%d' % tc)
    for i in range(len(result)):
        if (i+1) % 10 == 0:
            print(result[i])
        else:
            print(result[i], end='')
    print()
