# https://www.acmicpc.net/problem/2941

A = ('c=','c-','dz=','d-','lj','nj','s=','z=')
B = input()
for i in A:
    # 문자열의 값을 A로 다 바꿔준다.
    B = B.replace(i, 'A')
# 그것이 몇개인지 출력해준다.
print(len(B))