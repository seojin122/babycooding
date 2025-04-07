# 2025-04-04 (sucess)
 
"""
힌트: count 쓰기

GPT
number = "9999"

#number = input()
num = list(map(int, number))
count = [0] * 10


for i in num:
    count[i] += 1  

six_nine = count[6] + count[9]
count[6] = count[9] = (six_nine + 1) // 2
print(max(count))
"""
    





number = input()
num = list(map(int, number))
count = [0] * 10 #0~9

for i in num:
    count[i] += 1

same = count[6] + count[9]
count[6] = count[9] = (same + 1) // 2

print(max(count))