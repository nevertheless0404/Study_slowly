# https://www.acmicpc.net/problem/25192

import sys
sys.stdin = open("/Users/yuyeong/Desktop/1일 1코딩/2022.08.02/인사성 밝은 곰곰이.txt")

# 1. 
n = int(input())
dic = {}
count = 0

for tc in range(n):
    word = input() # 입장한 사람 
    if word == "ENTER": # Enthe가 입력되면 
        for key, value in dic.items(): # 딕셔너리 키와 벨류 전부 뽑음
            if value ==1:  
                count += 1 # 값을 +1 추가 
        dic ={}   
        
    else:
        if word not in dic:    # 존재하지 않으면 
            dic[word] = 1      # 1만 추가 
for key, value in dic.items():
    if value == 1:
        count += 1
print(count)


# 2. 
# n = int(input())
# gom = 0
# set_ = []
# for i in range(n):
#     log_list = input()
#     if log_list == "ENTER":
#         set_.clear()
#     else:
#         if log_list not in set_:
#             set_.append(log_list)
#             gom += 1
# print(gom)
