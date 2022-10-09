from collections import deque

chain = []
for i in range(4):
    chain.append(list(map(int, input())))

number = deque()
rotation = deque()

K = int(input())
for i in range(K):
    n, r = map(int, input().split())
    number.append(n)
    rotation.append(r)


def rotate(num, dir):

    # 시계방향 회전 뒤에서 빼서 맨 앞으로 넣어주기
    if dir == 1:
        temp = chain[num-1].pop(-1)
        chain[num-1].insert(0, temp)

    # 시계 반대방향 회전 앞에서 빼서 맨 뒤로 넣어주기
    elif dir == -1:
        temp = chain[num-1].pop(0)
        chain[num-1].append(temp)

    return None

# 1번에 2번 idx and 2번에 6번 idx
# 2번에 2번 idx and 3번에 6번 idx
# 3번에 2번 idx and 4번에 6번 idx

total_score = 0 
score = [1,2,4,8]

while rotation:
    # 다음 회전시킬 톱니바퀴
    num = number.popleft()
    # 다음 회전시킬 방향
    rot = rotation.popleft()

    # 1번 체인을 돌린다면 2->3->4 연쇄확인
    if num == 1:
        # 2번이랑 극이 같아서 안 돌아가면
        if chain[0][2] == chain[1][6]:
            # 1번만 돌린다
            rotate(1, rot)
        # 2번이랑 극이 다르다면
        else:
            # 1번 일단 돌리고
            rotate(1, rot)
            # 2,3번 극이 같아서 안 돌아가면
            if chain[1][2] == chain[2][6]:
                # 2번까지만 돌린다
                rotate(2, -rot)
            # 2,3번 극이 다르다면
            else:
                # 일단 2번 돌리고
                rotate(2, -rot)
                # 3,4번 극이 같다면
                if chain[2][2] == chain[3][6]:
                    # 3번은 1번과 같은 방향으로
                    rotate(3, rot)
                # 3,4번 극이 다르다면
                else:
                    # 3번 4번 돌리기
                    rotate(3, rot)
                    rotate(4, -rot)

    elif num == 2:
        # 2번이랑 1번 극이 같고 2번이랑 3번 극이 같으면
        if chain[1][6] == chain[0][2] and chain[1][2] == chain[2][6]:
            # 2번만 돌린다
            rotate(2, rot)

        # 2번이랑 1번만 같을 때
        elif chain[1][6] == chain[0][2] and chain[1][2] != chain[2][6]:
            # 일단 2번 돌리고
            rotate(2, rot)
            # 3번 4번이 같아서 안 돌아가면
            if chain[2][2] == chain[3][6]:
                rotate(3, -rot)
            # 4번도 돌려야하면
            else:
                rotate(3, -rot)
                rotate(4, rot)

        # 2번이랑 3번만 같으면
        elif chain[1][6] != chain[0][2] and chain[1][2] == chain[2][6]:
            # 1번 2번만 돌려준다
            rotate(2, rot)
            rotate(1, -rot)

        # 2번이랑 1번 3번 모두 다를 때
        else:
            # 일단 1번 2번 돌리고
            rotate(2, rot)
            rotate(1, -rot)

            # 3번 4번이 같아서 안 돌아가면
            if chain[2][2] == chain[3][6]:
                rotate(3, -rot)
            # 4번도 돌려야하면
            else:
                rotate(3, -rot)
                rotate(4, rot)

    elif num == 3:
        # 3번이랑 4번 극이 같고 3번이랑 2번 극이 같으면
        if chain[2][2] == chain[3][6] and chain[2][6] == chain[1][2]:
            # 3번만 돌린다
            rotate(3, rot)

        # 3번이랑 4번만 같을 때
        elif chain[2][2] == chain[3][6] and chain[2][6] != chain[1][2]:
            # 일단 3번 돌리고
            rotate(3, rot)

            # 1번 2번이 같아서 안 돌아가면
            if chain[0][2] == chain[1][6]:
                # 2번만 돌린다
                rotate(2, -rot)

            # 1번도 돌려야하면
            else:
                rotate(2, -rot)
                rotate(1, rot) 
            
        # 2번이랑 3번만 같을 때
        elif chain[2][2] != chain[3][6] and chain[2][6] == chain[1][2]:
            # 일단 3번 돌리고
            rotate(3, rot)
            rotate(4,-rot)
    
        else:
            # 일단 3번 4번 돌리고
            rotate(3, rot)
            rotate(4, -rot)

            # 1번 2번이 같아서 안 돌아가면
            if chain[0][2] == chain[1][6]:
                rotate(2, -rot)
            # 1번도 돌려야하면
            else:
                rotate(2, -rot)
                rotate(1, rot)


    else: 
        # 3번이랑 극이 같아서 안 돌아가면
        if chain[2][2] == chain[3][6]:
            # 4번만 돌린다
            rotate(4, rot)
        # 3번이랑 극이 다르다면
        else:
            # 4번 일단 돌리고
            rotate(4, rot)
            # 2,3번 극이 같아서 안 돌아가면
            if chain[1][2] == chain[2][6]:
                # 3번까지만 돌린다
                rotate(3, -rot)
            # 2,3번 극이 다르다면
            else:
                # 일단 3번 돌리고
                rotate(3, -rot)
                # 1,2번 극이 같다면
                if chain[0][2] == chain[1][6]:
                    # 4번은 2번과 같은 방향으로
                    rotate(2, rot)
                # 3,4번 극이 다르다면
                else:
                    # 3번 4번 돌리기
                    rotate(2, rot)
                    rotate(1, -rot) 


for i in range(4):   
    if chain[i][0] == 1:
        total_score+=score[i]

print(total_score)
        
      

   
