# https://www.acmicpc.net/problem/1065

n = int(input())
han = 0
for i in range(1, n+1):
    if i < 100:
        han += 1
    else:
        # 문자를 리스트 값으로 문자열로 나눠준다.
        ns = list(map(int, str(i)))
        # 등차수열, 첫번째 숫자, 두번재 숫자의 차와
        # 두번쨰 숫자와 세번째 숫자의 차이가 같으면 
        # 증가
        if ns[0] - ns[1] == ns[1] - ns[2]:
            han += 1
print(han)
