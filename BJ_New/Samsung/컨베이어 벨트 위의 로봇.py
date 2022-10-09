from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([False]*N)

cnt = 1
while True:

    # 1단계 벨트와 로봇 회전
    belt.rotate(1)
    robot.rotate(1)

    # 로봇이 내리는 위치에 온다면 내린다.
    robot[-1] = False

    # 2단계 로봇이 컨베이어 위에 있다면 이동
    if True in robot:
        # 먼저 올라간 로봇부터
        for i in range(N-2, -1, -1):
            # 현재 위치에 로봇이 있고 그 다음 위치에 로봇이 없으며, 내구도가 1 이상일 때
            if robot[i] == True and robot[i+1] == False and belt[i+1] >= 1:
                robot[i+1] = True
                robot[i] = False
                belt[i+1] -= 1

            # 로봇이 내리는 위치에 온다면 내린다.
            robot[-1] = False

    # 3단계 로봇을 올린다.
    if belt[0] >= 1:
        robot[0] = True
        belt[0] -= 1

    # 4단계 내구도 점검
    if belt.count(0) >= K:
        break

    cnt += 1

print(belt)
print(cnt)
