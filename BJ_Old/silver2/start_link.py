N = int(input())

member = []
visited = [0]*(N+1)
result = 100000000

for i in range(N):
    temp = list(map(int, input().split()))
    member.append(temp)


for i in range(N):
    for j in range(N): 
        
        if i == j:
            continue 
        
        start = member[i][j]
        link = member[j][i]
        diff = abs(start-link)

        if result > diff:
            result = diff

        print("start: ",start," link: ",link,"diff: ",diff)

print(result)
