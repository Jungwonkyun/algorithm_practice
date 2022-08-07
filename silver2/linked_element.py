# Code by 정원균
# BaekJoon #11724
import sys
sys.setrecursionlimit(10000)


def dfs(node):
    visited[node] = 1

    for e in graph[node]:
        print(visited)
        if visited[e] == 0:
            dfs(e)

    return None


node, edge = map(int, input().split())
visited = [0]*(node+1)
graph = [[] for _ in range(node+1)]
connect = 0

for i in range(edge):
    node_1, node_2 = map(int, input().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

for j in range(1, node+1):
    if visited[j] == 0:
        dfs(j)
        connect += 1

print(connect)
