# https://www.acmicpc.net/problem/11652

from multiprocessing.connection import answer_challenge
import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.07/카드.txt")

n = int(input())
dict = {}

for i in range(n):
    num = int(input())
    if num not in dict.keys():
        print(dict.keys())
        dict[num] = 1
    else:
        dict[num] += 1
    
max_num = max(list(dict.values()))

answer = []

for num, value in dict.items():
    if value == max_num:
        answer.append(num)

print(min(answer))