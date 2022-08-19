# https://www.acmicpc.net/problem/2511

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.19/카드놀이.txt")

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_card = 0
b_card = 0

win = 'D'

for i in range(10):
    if a[i] == b[i]:
        a_card += 1
        b_card += 1
    
    if a[i] > b[i]:
        a_card += 3
        win = 'A'
    
    if a[i] < b[i]:
        b_card += 3
        win = 'B'

if a_card > b_card:
    print(a_card, b_card)
    print('A')
if a_card < b_card:
    print(a_card, b_card)
    print('B')

if a_card == b_card:
    if win == 'A':
        print(a_card, b_card)
        print('A')
    if win == 'B':
        print(a_card, b_card)
        print('B')
    if win == 'D':
        print(a_card, b_card)
        print('D')




