from collections import deque
N, K = map(int, input().split())


def bfs():

    q = deque()
    q.append(N)

    while q:
        x = q.popleft()
        if x == K:
            print(dist[K])
            break
        
        next_list = [x-1, x+1, 2*x]

        for item in next_list:
            if 0 <= item <= Max and dist[item] == 0:
                q.append(item)
                dist[item] = dist[x]+1
    return None


Max = 10**5
dist = [0]*(Max+1)
bfs()
