N = int(input())

num = [0]*10000001
num[1] = 1
num[2] = 2

for i in range(3,N+1):
    num[i] = (num[i-2]+num[i-1]) % 15746
    
print(num[N])


