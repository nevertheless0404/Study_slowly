# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QLkdKAz4DFAUq

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.10/연월일 달력.txt")

t = int(input())
days = {1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for _ in range(1, t+1):
    data = str(input())
    year = data[0:4]
    month = data[4:6]
    day = data[6:8]

    answer = ''
    if 0 < int(month) < 13 and 0 < int(day) <= days[int(month)]:
        answer = year + '/' + month + '/' + day
    else:
        answer += '-1'
    
    print("#" + str(_) + " " + answer)

    



