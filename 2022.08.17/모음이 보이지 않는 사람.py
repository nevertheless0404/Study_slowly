# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcD_66pUEDFAV8

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.17/모음이 보이지 않는 사람.txt")

t = int(input())
for tc in range(1, t+1):
    word = input()
    result = ''
    for i in range(len(word)):
        if word[i] in ['a','e','i','o','u']:
            # continue 이하의 문은 수행하지 않고 다시 반복문
            # 조건식을 판단 위 리스트에 있는것이 빠지고 
            # 나오게 된다! 
            continue
        result += word[i]
    print('#%d %s' % (tc, result))
        
