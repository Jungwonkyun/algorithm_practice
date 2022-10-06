from collections import deque

n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
wait = []
bridge = [0]*w

for trk in truck:
    wait.append(trk)

weight = 0
total_time = 0

while True:

    out = bridge.pop(0)
    total_time += 1
    weight -= out

    if wait:
        next_truck = wait[0]

        # 다리에 다음 트럭이 들어갈 수 있으면
        if sum(bridge)+next_truck <= L:
            bridge.append(next_truck)
            wait.pop(0)

        # 다리에 다음 트럭이 들어갈 수 없다면
        else:
            bridge.append(0)

    if not bridge:
        break

print(total_time)
