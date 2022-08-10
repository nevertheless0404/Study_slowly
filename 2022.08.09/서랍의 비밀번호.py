# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QJ_8KAx8DFAUq

p, k = map(int, input().split())
count = 0
for i in range(k, p+1):
    count += 1
    if i == p:
        print(count)
        break