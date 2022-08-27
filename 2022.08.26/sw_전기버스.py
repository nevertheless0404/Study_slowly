# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.26/sw_전기버스.txt")

t = int(input())
for tc in range(1, t+1):
    k, n, m = map(int, input().split())
    num_b = list(map(int, input().split()))

    loc = 0 # 현재 위치
    char = 0  # 충전 횟수

    # 현재 위치 + 충전 후 이동할 수 있는 정류장 수 
    while loc + k < n:
        # 최대 기동 가능한 거리내에 충전소가 있는지 확인
        for i in range(k, 0, -1):
            if(loc + i) in num_b:
                # 충전소가 있을 경우 현재 위치에 더해 줌 
                loc += i
                # 충전 횟수 증가
                char += 1
                break
        # 최대 이동 거리 내에 충전소가 없는 경우 
        else:
            # 충전소 횟수 0
            char = 0
            break
    print('#{} {}'.format(tc, char))
            