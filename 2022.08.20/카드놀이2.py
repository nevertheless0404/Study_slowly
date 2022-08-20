# https://www.acmicpc.net/problem/10816

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.20/카드놀이2.txt")

n = int(input())
card_n = list(map(int, input().split()))

m = int(input())
card_m = list(map(int, input().split()))

# 숫자 카드를 딕셔너리에 넣어주기 
dict_n = dict()

for i in card_n:
    if i in dict_n:
        dict_n[i] += 1
    else:
        dict_n[i] = 1

for i in card_m:
    if i in dict_n:
        print(dict_n[i], end=" ")
    else:
        print(0, end = " ")