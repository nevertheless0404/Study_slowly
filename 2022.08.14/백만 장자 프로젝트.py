# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.14/백만 장자 프로젝트.txt")


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    n_sell = list(map(int, input().split()))

    # 맨 끝에 값을 최대값으로 지정
    max_sell = n_sell[-1]
    cnt = 0

    # 맨 뒤에서 부터 0번째 인덱스까지 1씩 감소하면서 반복 순회 
    for i in range(n-2, -1, -1):
        # 현재 매매가가 최대값보다 크면 변경 
        if n_sell[i] >= max_sell:
            max_sell = n_sell[i]
        # 현재 매매가가 최대값보다 크지 않으면 차익을 cnt에 더함 
        else:
            cnt += max_sell - n_sell[i]
    
    print('#{} {}'.format(tc, cnt))