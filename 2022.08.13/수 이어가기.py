# https://www.acmicpc.net/problem/2635

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.13/수 이어가기.txt")

# 첫번째 양수
n = int(input())
# 최대 개수와 수 리스트 만들어 주기
max_list = []
for i in range(1, n + 1):
    # 첫번째 수 넣기
    first_num = [n]
    first_num.append(i)
    # 첫번째 수가 있으므로 1부터 
    cnt = 1
    while True:
        # 만약 두번째 수가 첫번째 수보다 크고
        # 음수가 나오면 끝! 나와!
        next_num = first_num[cnt - 1] - first_num[cnt]
        if next_num < 0:
            break
        # 그렇지 않으면 추가
        first_num.append(next_num)
        cnt += 1

    if len(max_list) < len(first_num):
        max_list = first_num

print(len(max_list))
for j in max_list:
    print(j, end=" ")

