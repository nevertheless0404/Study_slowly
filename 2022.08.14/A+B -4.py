# https://www.acmicpc.net/problem/10951

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break

# try 구문 쪽에는 에러가 발생할 수 있는 코드를 작성
# except는 예외 발생시 실행할 코드를 작성 