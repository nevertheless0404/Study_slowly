# https://www.acmicpc.net/problem/1302

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.20/베스트셀러.txt")

n = int(input())
books = {}

for i in range(n):
    a = input()
    # 딕셔너리 값안에 책이 들어가 있으면 
    # 증가!
    if a in books:
        books[a] += 1
    else:
        books[a] = 1
# 책을 넣을 리스트 값
list = []

# 가장 많이 팔린 책 
num = max(books.values())
# print(num) 4

for i in books:
    if num == books[i]:
        list.append(i)

# 사전 순으로 정렬
list.sort()
# 가장 앞에 있는 것을 출력 
print(list[0])