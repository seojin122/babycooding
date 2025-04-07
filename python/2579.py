# 덕성 학습공통체 2주차 백준

#계단 갯수
n= int(input())
#개단 점수
s = [int(input()) for _ in range(n)]

#초기화
step=[0] * n

if n == 1:
    print( s[0] )
elif n == 2:
    print(s[0] + s[1])
else:
    step[0] = s[0]
    step[1] = s[0] + s[1]
    step[2] = max(s[0]+s[2], s[1]+s[2])
    for i in range(3,n):
        step[i] = max(step[i-3] + s[i-1] + s[i], step[i-2] + s[i])
    print(step[-1])



