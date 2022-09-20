#Code by 정원균 
#BaekJoon #2606 

from collections import deque

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

q = deque()
q.append(1)

visited[1] = 1

while q:

    current_node = q.popleft()

    for i in graph[current_node]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1
            cnt += 1

print(cnt)
