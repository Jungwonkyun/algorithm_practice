# Code by 정원균
# BaekJoon #1260
from collections import deque


def DFS(map_list, visited, vertex):

    visited[vertex] = 1
    print(vertex, end=" ")

    for vtx in map_list[vertex]:
        if visited[vtx] == 0:
            DFS(map_list, visited, vtx)
    return None


def BFS(map_list, visited, vertex, q):

    q.append(vertex)
    visited[vertex] = 1

    while q:

        current_node = q.popleft()
        print(current_node, end=" ")

        for vtx in map_list[current_node]:
            if visited[vtx] == 0:
                q.append(vtx)
                visited[vtx] = 1

    print()
    return None


node, edge, vertex = map(int, input().split())
map_list = [[] for _ in range(node+1)]


for i in range(edge):
    v1, v2 = map(int, input().split())
    map_list[v1].append(v2)
    map_list[v2].append(v1)


for i in range(node+1):
    if len(map_list[i]) > 1:
        map_list[i].sort()


visited = [0]*(node+1)
DFS(map_list, visited, vertex)
print()

visited = [0]*(node+1)
bfs_q = deque()
BFS(map_list, visited, vertex, bfs_q)
