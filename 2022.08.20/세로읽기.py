# https://www.acmicpc.net/problem/10798

from socket import IPV6_RTHDR_TYPE_0
import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.20/세로읽기.txt")

words = []
length = []

for _ in range(5):
    word = input()
    words.append(word)
    length.append(len(word))
    print(length)

result = ''
for i in range(max(length)):
    print(i)
#     for j in range(5):
#         if i < length[j]:
#             result += words[j][i]
# print(result)