# https://www.acmicpc.net/problem/4344

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.14/평균은 넘겠지.txt")

c = int(input())

for _ in range(c):
    num = list(map(int, input().split()))
    # 평균을 구하기 위해 1번쨰 요소부터 마지막 까지 더한 다음, 학생수로 나눠줌
    avg = sum(num[1:])/num[0]

    cnt = 0
    for i in num[1:]:
        if i > avg:
            cnt += 1
    
    per = (cnt/num[0])*100
    print('%.3f' %per + '%')