# https://www.acmicpc.net/problem/1764

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.20/듣보잡.txt")

n, m = map(int, input().split())

arr_n = set()
arr_m = set()

for _ in range(n):
    arr_n.add(input())
    # print(arr_n)
    # {'ohhenrie'}
    # {'ohhenrie', 'charlie'}
    # {'ohhenrie', 'charlie', 'baesangwook'}

for _ in range(m):
    arr_m.add(input())
    # print(arr_m)
    # {'obama'}
    # {'obama', 'baesangwook'}
    # {'ohhenrie', 'obama', 'baesangwook'}
    # {'ohhenrie', 'clinton', 'obama', 'baesangwook'}

# 교집합을 구해서 갯수 찾기 
arr = sorted(list(arr_n & arr_m))
print(len(arr))

for i in arr:
    print(i)