# https://www.acmicpc.net/problem/2562

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.14/최댓값.txt")

numbers = []
for _ in range(9):
    i = int(input())
    numbers.append(i)
    
print(max(numbers))
print(numbers.index(max(numbers))+1)