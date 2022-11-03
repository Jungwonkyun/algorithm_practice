test_case = int(input())

for t in range(1, test_case+1):
    N, M = map(int, input().split())
    route = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        route[a].append(b)
        route[b].append(a)

    result = 0
    for i in range(1, N+1):
        visited = [False]*(N+1)

        def dfs(v, count):
            global result
            visited[v] = True
            result = max(result, count)
            for node in route[v]:
                if visited[node] == False:
                    dfs(node, count+1)
                    # 같은 정점 다시 돌아야 하니까 다시 방문처리 초기화 해야한다.
                    visited[node] = False
        dfs(i, 1)

    print("#{} {}".format(t, result))
