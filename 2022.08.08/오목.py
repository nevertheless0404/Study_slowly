# https://www.acmicpc.net/problem/2615

import sys
sys.stdin = open ("/Users/yuyeong/Desktop/1일 1코딩/2022.08.08/오목.txt")

omok = [list(map(int, input().split())) for _ in range(19)]

di = [-1,0,1,1]
dj = [1,1,1,0]

for i in range(19):
    for j in range(19):
        # 승부가 결정나지 않았을 떄는 0!
        if omok[i][j] != 0:
            
            # 현재 좌표에서 해당 방향으로 1만큼 이동 
            for k in range(4):
                cnt = 1 
                ni = i + di[k]
                nj = j + dj[k]

                # 반복문을 통해 오목이 되는지 확인 
                # 오목이 되면 증가 
                while 0 <= ni < 19 and 0 <= nj < 19 and omok[ni][nj] == omok[i][j]:
                    cnt += 1
                    
                    if cnt == 5:
                        # 첫번째 바둑돌 보다 한 칸 이전의 바둑돌 체크
                        if 0 <= i - di[k] < 19 and 0 <= j - dj[k] < 19 and omok[i - di[k]][j - dj[k]] == omok[i][j]:
                            break
                        # 마지막 바둑돌보다 한 칸 이후의 바둑돌 체크 
                        if 0 <= ni + di[k] < 19 and nj + dj[k] < 19 and omok[ni + di[k]][nj + dj[k]] == omok[i][j]:
                            break
                        
                        # 육목이 아니면 성공!! 종료종료 
                        print(omok[i][j])
                        print(i + 1, j + 1)
                        exit()
                    ni += di[k]
                    nj += dj[k]
print(0)

