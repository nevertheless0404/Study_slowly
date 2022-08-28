# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.28/sw_숫자카드.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    card = list(input())
    cnt = [0] * 10

    for i in range(n):
        cnt[int(card[i])] += 1
        print(cnt)

    max_num = 0

    # 큰 숫자 저장 리스트
    idx=[]

    for j in range(len(cnt)):
        if max_num <= cnt[j]:
           max_num = cnt[j]
           idx.append(j)
    
    print('#{} {} {}'.format(tc, idx.pop(), max_num))

