# #2606 virus solved with DFS

num_computer = int(input())
pair_computer = int(input())
cnt = 0

graph = [[]*num_computer for _ in range(num_computer+1)]
visited = [0]*(num_computer+1)

for _ in range(pair_computer):

    # split()으로 쪼개면 str로 받는데 map(int,split())으로 숫자로 바로 바꿀 수 있다.
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#[ [] [2,5] [1,3,5] [2] [7] [1,2,6] [5] [4] ]

def dfs(node):
    global cnt
    visited[node] = 1

    for i in graph[node]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


dfs(1)

print(cnt)
