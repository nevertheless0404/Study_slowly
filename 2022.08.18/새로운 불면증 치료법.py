# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.18/새로운 불면증 치료법.txt")

# 10 크기의 배열을 선언하고 각 n의 배수의 자리수를 체크
# ex) n = 1234
# cnt = 1, cnt*n 은 1234 체크된 수는 1,2,3,4
# cnt = 2, cnt*n 은 2468 이전에 체크된 수와 함께 1,2,3,4,6,8

for tc in range(int(input())):
    n = int(input())
    # 중복이 허용되지 않음 
    coll = set()
    # 배열에 숫자가 나올때 마다 1로 체크
    cnt = 1

    while True:
        # 중복을 허용하지 않고 문자형태로 
        # 넣어주고, 10개가 되면 나온다.
        for num in list(str(n)):
            coll.add(num)
        if len(coll) == 10:
            break
        n //= cnt
        cnt += 1
        # 센 양의 수 
        n *= cnt
    print('#{} {}'.format(tc+1,n))
