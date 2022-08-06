# https://www.acmicpc.net/problem/1302

from itertools import tee
import sys
sys.stdin = open("/Users/yuyeong/Desktop/1일 1코딩/2022.08.06/베스트셀러.txt")

n = int(input())
books = {}
for tc in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        # 들어가 있으면 계속 더해주기 
        books[book] += 1

# 제일 큰 값 구해주기 
target = max(books.values())
# 리스트 초기화
arr = []


for book, number in books.items():
    if number == target:
        arr.append(book)
print(book)
print(sorted(arr)[0])

    


