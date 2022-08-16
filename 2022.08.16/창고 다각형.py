# https://www.acmicpc.net/problem/2304

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.16/창고 다각형.txt")


n = int(input())
lst = []
result = 0
for i in range(n):
    a, b = map(int, input().split())
    lst.append([a,b])
# 기둥을 X축 순으로 정렬 
lst.sort()

# 가장 높은 기둥 찾기
i = 0
for j in lst:
    if j[1] > result:
        result = j[1]
        idx = i
    i += 1

# 첫번째 기둥의 높이 알아보기 
height = lst[0][1]

# 최대 높이전까지 돌면서 다음 기둥이 높으면 
# result 값에 면적 + 높이를 갱신  
for i in range(idx):
    if height < lst[i+1][1]:
        result += height * (lst[i+1][0] - lst[i][0])
        height = lst[i+1][1]
    else:
        result += height * (lst[i+1][0] - lst[i][0])

# 맨 뒤에도 똑같이 
height = lst[-1][1]

for i in range(n-1, idx, -1) :
    if height < lst[i-1][1] :
        result += height * (lst[i][0]-lst[i-1][0])
        height = lst[i-1][1]
    else :
        result += height * (lst[i][0] - lst[i-1][0])

print(result)