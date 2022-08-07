# Code by 정원균
# BaekJoon #11724
import sys
sys.setrecursionlimit(10000)

def dfs(node):

    visited[node] = 1

    for i in graph[node]:
        if visited[node] == 0:
            dfs(i)

    print(visited)
    return None


node, edge = map(int, input().split())
visited = [0]*10
graph = [[] for _ in range(1001)]
connect = 0

for i in range(edge):
    
    node_1, node_2 = map(int, input().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

for i in range(1,node+1):
    
    if visited[i] == 0:
        dfs(i)
        connect+=1
        

print(connect)