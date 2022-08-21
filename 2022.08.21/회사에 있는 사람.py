# https://www.acmicpc.net/problem/7785

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.21/회사에 있는 사람.txt")

n = int(input())
temp = dict ()

# 반복문을 통해 출,퇴근의 기록을 확인
for _ in range(n):
    a, b = map(str, input().split())

    # 출근했으면 딕셔너리로 받는다
    if b == 'enter':
        temp[a] = b
    # 퇴근했으면 삭제!
    else:
        del temp[a]

temp = sorted(temp.keys(), reverse=True)

for i in temp:
    print(i)