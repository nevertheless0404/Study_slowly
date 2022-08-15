# https://www.acmicpc.net/problem/2116

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.15/주사기 쌓기.txt")

num_dice = int(input())
dice = []
for _ in range(num_dice):
    dice.append(list(map(int, input().split())))

route = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2,  5 : 0}
max_num = 0
# 첫 번째 주사위를 기준으로 1~6 모두 순회
for i in range(6):
    # 옆면의 최대값을 저장해둘 리스트
    result = []
    # 주사위 각면에 써져있는 숫자
    tmp = [1, 2, 3, 4, 5, 6]
    # 주사위 아랫면 숫자 제거 
    tmp.remove(dice[0][i])
    # 윗면 값 계산 
    next = dice[0][route[i]]
    # 주사위 윗면 값 삭제
    tmp.remove(next)
    # 옆면들 중 가장 큰 값 삽입
    result.append(max(tmp))
    for j in range(1, num_dice):
        tmp = [1, 2, 3, 4, 5, 6]
        tmp.append(next)
        # 현재 주사위 윗면 계산 
        next = dice[j][route[dice[j].index(next)]]
        tmp.remove(next)
        result.append(max(tmp))
    result = sum(result)
    # 이전의 최대값과 현재의 최대값을 비교해여 더 큰 값을 저장 
    if max_num < result:
        max_num = result

print(max_num)