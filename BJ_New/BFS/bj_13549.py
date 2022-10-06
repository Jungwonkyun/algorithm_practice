from collections import deque

N, K = map(int, input().split())
Max = 10**5
distance = [0]*(Max+1)
visited = [False]*(Max+1)


def bfs(N):

    q = deque()
    q.append(N)

    if N == K:
        return

    while q:
        x = q.popleft()

        next_list = [2*x, x-1, x+1]

        for i in range(len(next_list)):
            if 0 <= next_list[i] <= Max and visited[next_list[i]] == False:
                if i == 1 or i == 2:
                    q.append(next_list[i])
                    distance[next_list[i]] = distance[x]+1
                    visited[next_list[i]] = True

                elif i == 0:
                    q.appendleft(next_list[i])
                    distance[next_list[i]] = distance[x]
                    visited[next_list[i]] = True

    return


bfs(N)
print(distance[K])
