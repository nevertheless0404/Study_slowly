# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
# 단, 주어질 숫자는 10000을 넘지 않는다.

n = int(input())
num = 0
for i in range(1, n+1):
    num += i
print(num)