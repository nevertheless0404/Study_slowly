# https://www.acmicpc.net/problem/2559

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.17/수열.txt")

n, k = map(int, input().split())
data = list(map(int, input().split()))

tmp = sum(data[:k])
result = tmp

for i in range(k, n):
    # 투 포인터와 슬라이딩 윈도우 활용 
    # 순간수간의 최대값을 저장하여 출력 
    tmp += data[i] - data[i-k]
    result = max(result, tmp)

print(result)