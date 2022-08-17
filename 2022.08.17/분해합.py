# https://www.acmicpc.net/problem/2231

n = int(input())
result = 0
for i in range(1, n+1):
    hap = list(map(int, str(i)))
    s = i + sum(hap)
    if (s == n):
        result += 1
        break
print(result)