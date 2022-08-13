# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.13/최빈수 구하기.txt")

t = int(input())
for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    # 학생수의 점수 
    data = [0] * 1001
    # 점수를 확인하고 그 값을 인덱스 해서 증가 
    for i in m:
        data[i] += 1
    # 최대값을 구하여 할당
    max_num = max(data)
    # 최빈수 값을 담기 위한 리스트
    result = []
    for j in range(len(data)):
        if data[j] == max_num:
            result.append(j)
   
    print('#%d %d' % (n, max(result)))




    