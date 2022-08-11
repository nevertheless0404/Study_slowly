# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QPRjqA10DFAUq

# 자연수를 문자열 형태로 입력받아 각 자리수를 정수형으로 변환
n = input()
result = 0
for i in range(len(n)):
    result += int(n[i])
print(result)