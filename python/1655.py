# 2025-04-01

# 가운데를 말해요

"""
N = int(input("정수의 갯수: "))
input_list=[]

for i in range(N):
    input_num = int(input("숫자 입력"))
    input_list.append(input_num)
    input_list = sorted(input_list)

    # 짝수
    if (len(input_list) % 2 == 0):
        print(input_list[(i//2) -1])

    # 1
    elif(len(input_list) == 1):
        print(input_num)

    #홀수
    elif (len(input_list) % 2 == 1):
        print(input_list[i//2])

    else:
        print("error")
"""

N = int(input(""))


input_list=[]
result_list=[]

for i in range(N):
    num = int(input())
    input_list.append(num)
    input_list.sort()


    mid_index = len(input_list) // 2

    # 짝수
    if (len(input_list) % 2 == 0):
        result_list.append(input_list[mid_index -1 ])


    #홀수
    elif (len(input_list) % 2 == 1):
        result_list.append(input_list[mid_index])


for k in range(len(result_list)):
    print(result_list[k])


