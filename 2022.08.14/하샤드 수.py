# https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    sum = 0
    for i in range(x):
        sum += int(i)
    if x % sum == 0:
        return True 
    else:
        return False
