# 덕성 학습공통체 1주차 백준

"""
문제
세준이는 성형수술을 한 후에 병원에 너무 오래 입원해 있었다. 이제 세준이가 병원에 입원한 동안 자기를 생각해준 사람들에게 감사하다고 말할 차례이다.

세준이를 생각해준 사람은 총 N명이 있다. 사람의 번호는 1번부터 N번까지 있다. 세준이가 i번 사람에게 인사를 하면 L[i]만큼의 체력을 잃고, J[i]만큼의 기쁨을 얻는다. 세준이는 각각의 사람에게 최대 1번만 말할 수 있다.

세준이의 목표는 주어진 체력내에서 최대한의 기쁨을 느끼는 것이다. 세준이의 체력은 100이고, 기쁨은 0이다. 만약 세준이의 체력이 0이나 음수가 되면, 죽어서 아무런 기쁨을 못 느낀 것이 된다. 세준이가 얻을 수 있는 최대 기쁨을 출력하는 프로그램을 작성하시오.
"""

"""
입력
첫째 줄에 사람의 수 N(≤ 20)이 들어온다. 둘째 줄에는 각각의 사람에게 인사를 할 때, 잃는 체력이 1번 사람부터 순서대로 들어오고, 셋째 줄에는 각각의 사람에게 인사를 할 때, 얻는 기쁨이 1번 사람부터 순서대로 들어온다. 체력과 기쁨은 100보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 세준이가 얻을 수 있는 최대 기쁨을 출력한다.
"""




N = int(input("사람의 수: "))
power = list(map(int, input("체력: ").split(" ")))
happy = list(map(int, input("기쁨: ").split(" ")))

if ( 0 < N <= 20 ) and ( len(power) == N) and (len(happy) == N) :
  pass
else:
  print("오류입니다.")
  exit()


# 2차원 리스트 생성
data = [list(x) for x in zip(power, happy)]

# happy 값이 체력대체 높은 기준으로 정렬
data=sorted(data,key=lambda x: -x[1]/x[0] if x[0] != 0 else float('inf'))

happy_to = 0
reject=100



for i in range(N):
    reject = reject - data[i][0]
    if (  reject <= 0  ):
        break
    else:
        happy_to = happy_to + data[i][1]



print(power)
print(happy)
print(data)
print(happy_to)



"""
data = [list(x) for x in zip(power, happy)]
2차원 리스트를 생성하는 부분입니다.

zip(power, happy) → 각 요소를 짝지어 튜플로 묶음.



zip([30, 10, 20], [3, 1, 2])
→ [(30, 3), (10, 1), (20, 2)]
list(x) for x in zip(...) → 튜플을 리스트로 변환하여 2차원 리스트 생성.

data = [[30, 3], [10, 1], [20, 2]]
"""


"""
data.sort(key=lambda x: x[0])
sort()를 사용하여 첫 번째 값(power)을 기준으로 정렬합니다.

lambda x: x[0] → 각 리스트의 첫 번째 원소(체력 값)를 기준으로 정렬.

정렬 전:
data = [[30, 3], [10, 1], [20, 2]]

정렬 후 (power 값 기준 오름차순):
data = [[10, 1], [20, 2], [30, 3]]
"""














