# https://www.acmicpc.net/problem/1157

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.19/단어공부.txt")

word = input().upper()
alp = list(word)
result = []
for i in alp:
    count = word.count(i)
    result.append(count)

if result.count(max(result)) >= 2:
    print("?")
else:
    print(alp[result.index(max(result))])