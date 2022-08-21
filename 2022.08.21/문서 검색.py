# https://www.acmicpc.net/problem/1543

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.21/문서 검색.txt")

n = input()
find = input()

# 단어 개수 
cnt = 0
# 인덱스 번호
index = 0

for i in range(len(n)):
    # 중복되는 단어를 포함하려고 할 때 건너뛰기
    if index > i:
        continue
    # 찾는 단어와 문서의 단어가 같을 때 증가
    if find == n[i: i+len(find)]:
        cnt += 1

        # 인덱스 번호는 동시에 셀 수 없는 가장 가까운 번호로 이동 
        index = i + len(find)
print(cnt)