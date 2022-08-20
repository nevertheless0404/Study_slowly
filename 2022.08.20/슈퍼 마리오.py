# https://www.acmicpc.net/problem/2851

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.20/슈퍼 마리오.txt")

mushroom = []
for i in range(10):
    mushroom.append(int(input()))

result = 0
for j in mushroom:
    result += j
    if result >= 100:
        # 100과 가까운 수를 구하고 멈춰
        if result - 100 > 100 - (result-j):
            result -= j
        break
print(result)
     