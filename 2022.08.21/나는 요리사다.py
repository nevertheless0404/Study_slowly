# https://www.acmicpc.net/problem/2953

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.21/나는 요리사다.txt")

score = []

for i in range(5):
    score.append(sum(map(int, input().split())))

# 최종적으로 총 점수가 가장 높은 우승자의 인덱스 값에 1을 더하고
# 그 사람이 얻은 점수를 출력 
print(score.index(max(score))+1 , max(score))