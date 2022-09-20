# Code by 정원균
# BaekJoon #1654

import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

start, end = 0, max(tree_list)  # 시작 점, 끝점

# 이분 탐색
while start <= end:
    mid = (start+end)//2
    tree = 0  # 잘린 나무 합

    for i in tree_list:
        if i > mid:  # mid보다 큰 나무 높이는 잘림
            tree += i - mid

    if tree >= M:  # 원하는 나무 높이보다 더 많이 잘렸으면
        start = mid + 1

    else:  # 원하는 나무 높이보다 덜 잘렸으면
        end = mid - 1

print(end)
