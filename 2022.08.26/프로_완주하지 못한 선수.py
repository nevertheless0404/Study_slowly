# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    # 각 이름의 hash 값을 구하고, 이 값들의 합 
    # Participant의 sum(hash) 구하기
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    
    # 완주자들 제외 시키기 
    # completion의 sum(hash) 빼기
    for comp in completion:
        sumHash -= hash(comp)
    
    # 남은 값이 완주하지 못한 선수의 hash 값이 된다
    return hashDict[sumHash]