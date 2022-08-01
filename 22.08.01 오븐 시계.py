# https://www.acmicpc.net/problem/2525

H,M = map(int, input().split())
timer = int(input())
# ex) 34//60 => 0
H = H + timer//60
# ex) 50%60 => 50
M += timer%60
if M >=60:
    H += 1
    M -= 60
if H >=24:
    H -=24

print('%d %d'% (H,M))