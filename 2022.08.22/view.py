# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.22/view.txt")

t = 10 
for tc in range(1, t+1):
    n = int(input())
    data = list(map(int, input().split()))
    result = 0

# 맨 왼쪽 두칸, 맨 오른쪽 두 칸은 건물이 지어지지 않음 
# 2qnxj n-2까지를 반복문의 범위로 설정
    for i in range(2, n-2):
        left = max(data[i-1], data[i-2])
        right = max(data[i+1], data[i+2])
        # 양방향 조망 확보!
        if data[i] - left > 0 and data[i] - right > 0:
            max_dir = max(left, right)
            result += data[i] - max_dir

    print('#%d %d'% (tc, result))