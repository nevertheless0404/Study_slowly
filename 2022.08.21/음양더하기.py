# https://school.programmers.co.kr/learn/courses/30/lessons/76501?language=python3

def soloution(absolutes, signs):
    # sings 가 참이면 해당 absoluted은 실제 정수가 양수, 거짓이면 음수 
    # 주어진 수에 하나씩 접근
    # 양수, 음수가 적용된 실제 합
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer 