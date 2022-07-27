#Code by 정원균 
#BaekJoon #15649

from itertools import permutations

N, M = map(int, input().split())
total_num = []

for i in range(1,N+1):
    total_num.append(i)

for i in permutations(total_num,M):
    for j in range(M):
        print(i[j],end = " ")
    print()

