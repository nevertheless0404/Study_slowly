# https://www.acmicpc.net/problem/2511

import sys
sys.stdin = open("/Users/yuyeong/Desktop/1일 1코딩/2022.08.06/카드놀이.txt")

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_score = 0
b_score = 0

win = 'D'


for i in range(10):
    # 비길 경우 
    if a[i] == b[i]:
        a_score += 1
        b_score += 1
    # A가 이길 경우 
    if a[i] > b[i]:
        a_score += 3
        win = 'A'
    if a[i] < b[i]:
        b_score += 3
        win = 'B'

# a와 b의 점수 비교 
if a_score > b_score:
    print(a_score, b_score)
    print('A')
if a_score < b_score:
    print(a_score, b_score)
    print('B')

# 스코어가 같을 경우 
if a_score == b_score:
    if win == 'A':
        print(a_score, b_score)
        print('A')
    if win == 'B':
       print(a_score, b_score)
       print('B') 
    if win == 'D':
        print(a_score, b_score)
        print('D')
