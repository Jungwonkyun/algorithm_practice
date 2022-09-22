import itertools

N = int(input())
number = list(map(int, input().split()))
op_info = list(map(int, input().split()))
oper = ["+","-","*","//"]
operator = []

for i in range(4):
    for j in range(op_info[i]):
        operator.append(oper[i]) 

#순열을 이용해서 모든 경우의 수 구하기
nPr = list(itertools.permutations(operator, len(operator)))

maximum = -(1e+10)
minimum = 1e+10 



for i in range(len(nPr)):
    result = number[0]
    temp = list(nPr[i])
    for j in range(1,N):

        
        if temp[j-1] == "+":
            result += number[j] 
        
        elif temp[j-1] == "-":
            result -= number[j] 
        
        elif temp[j-1] == "*":
            result *= number[j]
        
        else:
            if result < 0:
                result = -int(((-result)//number[j]))
            else:
                result = int(result//number[j])


    if result > maximum:
        maximum = result
    
    if result < minimum:
        minimum = result
    

print(maximum)
print(minimum)

