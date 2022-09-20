# Code by 정원균
# BaekJoon #1654

import sys
sys.setrecursionlimit(10000)

K, N = map(int, input().split())
lan_list = []

for i in range(K):
    lan_list.append(int(input()))

start, end = 1, max(lan_list)
mid = (start+end)//2


while start <= end:
    num_lan = 0
    mid = (start+end)//2

    for lan in lan_list:
        num_lan += (lan//mid)

    if num_lan >= N:
        start = mid+1

    else:
        end = mid-1

print(end)
