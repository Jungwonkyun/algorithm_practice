# Code by 정원균
# BaekJoon #1541

Data = input().split(sep="-") #input expression 

result = 0

for i in Data[0].split("+"):
    result+=int(i)

for i in Data[1:]:
    for j in i.split("+"):
        result-=int(j)

print(result)