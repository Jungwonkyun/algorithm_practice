
N = int(input())

total = 0
length = len(str(N))

#자리수 이하의 계산 처리 ex) 154 => 9까지 + 10~99까지 자리수 계산
for i in range(length-1):
    total += (i+1)*9*10**i

#현재 자리수에서 계산 ex) 154 - 100 => 55개 x 3 155자리 
total += length*(N-10**(length-1)+1)
    
print(total)

