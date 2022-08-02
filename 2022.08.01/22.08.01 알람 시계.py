# https://www.acmicpc.net/problem/2884

H, M = map(int, input().split())
# 45분 이상이면 -45분 
if M >= 45:
    print(H, M-45)
    # ex) 10 10 => 9 25 은 시간에서 -1, +15한 시간
elif H >= 1 and M <= 44:
    print(H-1, M+15)
    # ex) 0 30 => 23 45은 시간에서 23, +15를 한 시간 
else:
    print(23, M+15)
