# https://www.acmicpc.net/problem/2628

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.15/종이자르기.txt")

c, r= map(int ,input().split())

# 자르는 위치 저장
list_c = [0, c]
list_r = [0, r]

for _ in range(int(input())):
    xy, cutnum = map(int, input().split())
    # 세로가 1 가로가 0
    if xy == 0:
        list_r.append(cutnum)
    else:
        list_c.append(cutnum)
    

list_c.sort()  # [0, 4, 10]
list_r.sort()  # [0, 2, 3, 8]
# print(list_c)
# print(list_r)

result_r = []  # [4, 6]
result_c = []  # [0, 2, 3, 8]

# 제일 큰 상자를 구하려는 식은 
# (8-3) * (10-4)
for i in range(len(list_c) -1):   # 0 1
    # list_c[1] - list_c[0]  list_c[2] - list[1]
    result_c.append(list_c[i+1]-list_c[i]) 
for j in range(len(list_r) -1):  # 0 1 2
    # list_r[1]-list_r[0] list_r[2]-list_[1] list_r[3]-list[2]
    result_r.append(list_r[j+1]-list_r[j])

print(max(result_r) * max(result_c))

        
        







