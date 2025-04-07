# 2025-04-03

#국회의원 숫자
N = int(input())

#국회의원 득표수
Score = [int(input()) for _ in range(N)]


if N == 1:
    print(0)
    exit()   
elif ( 1 < N < 51 ):
    pass
else:
    exit()

money = 0


while True:
    others = Score[1:]
    max_index = others.index(max(others)) + 1

    if  max(others) < Score[0]:
        break

    else:
        money += 1
        Score[max_index] -= 1
        Score[0] += 1
 
print(money)
