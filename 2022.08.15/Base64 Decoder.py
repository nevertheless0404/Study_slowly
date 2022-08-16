# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PR4DKAG0DFAUq

from curses.panel import top_panel
import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.15/Base64 Decoder.txt")

# 1. 아스키코드 : chr -> ord로 바꾸기
# 2. 10 진수 -> 2진수, 8비트로 표현
# 3. 8비트로 읽던걸 6비트로 -> 숫자 계산
# 4. 그 수에 대응되는 알파벳으로 인코딩 된것 
# 5. 디코딩은 거꾸로!!

d = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,
     "K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,
     "U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25,"a":26,"b":27,"c":28,"d":29,
     "e":30,"f":31,"g":32,"h":33,"i":34,"j":35,"k":36,"l":37,"m":38,"n":39,
     "o":40,"p":41,"q":42,"r":43,"s":44,"t":45,"u":46,"v":47,"w":48,"x":49,
     "y":50,"z":51,"0":52,"1":53,"2":54,"3":55,"4":56,"5":57,"6":58,"7":59,
     "8":60,"9":61,"+":62,"/":63}
for tc in range(int(input())):
    S = input()
    temp = ''
    result = ''
    for character in S:
        tobinary = bin(d[character])[2:]
        if len(tobinary) < 6:
            tobinary = "0"*(6-len(tobinary)) + tobinary
        temp += tobinary
    for i in range(0,len(temp),8):
        result+= chr(int('0b'+temp[i:i+8],2))
    print("#{} {}".format(tc+1, result))