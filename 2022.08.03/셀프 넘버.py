# https://www.acmicpc.net/problem/4673

n = set(range(1, 10001))
number = set()

# i = 850
for i in range(1, 10001):
    # j = 8, 5, 0
    for j in str(i):
        # 850 + 8 + 5 + 0 , i = 863
        i += int(j)
        # 생성자가 있는 숫자
    number.add(i)
n = sorted(n - number)
for k in n:
    print(k)