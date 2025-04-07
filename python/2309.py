# 2025-04-02


"""
1. Combination

조합의 순서를 고려하지 않고 n개 중에 r개를 뽑는 경우를 말한다.
리턴값: 반복자, 튜플


"""




from itertools import combinations

#list_1 =[20, 7, 23, 19, 10, 15, 25, 8, 13]
dwarfs = [int(input()) for _ in range(9)]
if(len(dwarfs) == 9):
    pass
else:
    exit()



for comb in combinations(dwarfs, 7):
    if(sum(comb) == 100):
        sorted_comb = sorted(comb)
        break

for k in sorted_comb:
    print(k)

        