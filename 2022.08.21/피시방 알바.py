# https://www.acmicpc.net/problem/1453

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.21/피시방 알바.txt")

n = int(input())
pc_num = list(map(int, input().split()))
# 피시방 자리
pc_postion = [0] * 101
# 거절당한 사람 
refusal = 0

for i in pc_num:
    # 피시방 자리에 사람이 있으면 
    if pc_postion[i] != 0:
        # 거절당한 사람 증가
        refusal += 1
    
    else:
        # 사람이 없으면 자리 앉아도 됌!
        pc_postion[i] += 1
print(refusal)