# 2025.03.24 ~ 2025.03.29: 베코 코딩 스터디 1번

"""
< 닭싸운 팀 정하기 >

닭싸움의 팀을 정하는 원칙

1. 내 친구의 친구는 내 친구이다.
2. 내 원수의 원수도 내 친구이다.

이 때 두 학생이 친구이면 같은 팀에 속해있어야 하며, 같은 팀에 속해 있는 사람들끼리는 전부 친구여야 한다.

학생들의 인간관계가 주어지면, 닭싸움을 위한 팀 정하기를 할 때, 최대 얼마나 많은 팀이 만들어질 수 있는지 알아내는 프로그램을 작성하시오.

"""


"""
입력: 

첫째 줄에 학생의 수 n이 주어진다. 각 학생들은 1부터 n까지 번호가 매겨져 있다. (2 ≤ n ≤ 1000) 

둘째 줄에 학생 간의 인간관계 중 알려진 것의 개수 m이 주어진다. (1 ≤ m ≤ 5000)

다음 m개의 줄에는 한 줄에 한 개씩, 학생 간의 인간관계가 F p q 혹은 E p q의 형태로 공백으로 구분되어 주어진다. (1 ≤ p < q ≤ n)

첫 번째 글자가 F인 경우에는 p와 q가 친구인 것이고, E인 경우는 p와 q가 원수인 경우이다. 

입력은 모순이 없음이 보장된다. 즉, 두 학생이 동시에 친구이면서 원수인 경우는 없다.



출력: 
첫째 줄에, 가능한 최대 팀 개수를 출력한다.
"""




n = int(input("학생수 n을 입력하세요: \n"))
m = int(input("학생들의 알려준 관계의 수를 입력하세요: \n"))


team = []
list_b=[]
new_list=[]

for i in range(m):
    input_ = input("학생들의 관계를 E/F p q 형식으로 입력해주세요: \n").split(" ")
    if len(input_) != 3:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue

    a, b, c = input_
    b, c = int(b), int(c)
    


    if(a == "F"):
      found = True
      for i in range(len(team)):
        for j in range(len(team[i])):
          if (b == team[i][j]) or (b == team[i]):
            team[i].append(c)
            found= False
            break
          elif (c == team[i][j]) or (c == team[i]):
            team[i].append(b)
            found= False
            break
          

      if found:
        team.append([b,c])


    elif(a == "E"):
      found = True
      list_b.append([b,c])
      
      for i in range(len(team)):
        for j in range(len(team[i])):
          if (b == team[i][j]) or (b == team[i]):
          
            found= False
            break



          elif (c  == team[i][j] or (c == team[i])):

            found= False
            break

          else:
            for i in range(len(list_b)):

              if b == list_b[i][1] :
                new_list.append(c)
                new_list.append(list_b[i][0])
                break
              
              elif b ==list_b[i][0]:
                new_list.append(c)
                new_list.append(list_b[i][1])
                break
                
              elif c == list_b[i][1]:
                new_list.append(b)
                new_list.append(list_b[i][0])
                break
              
                
              elif c ==list[b]:
                new_list.append(b)
                new_list.append(list_b[i][1])
                break
    
                
              else:
                pass
                




            if new_list:
              for i in range(len(team)):
                for j in range (len(team[i])):
                  if new_list[0] == team[i][j] or new_list[0] == team[i]:
                    team[i].append(new_list[1])
                    found= False
                    break
                  elif new_list[1] == team[i][j] or new_list[1] == team[i][j]:
                    team[i].append(new_list[0])
                    found= False
                    break
                  else:
                    pass




      if found:
        team.append([b])
        team.append([c])

      




print("list_b: ", list_b)
print("new_list: ", new_list)

print(team)

print(len(team))


