r, c, k = map(int, input().split())
array = []


def R_operation():

    length = 0
    # 모든 행에 대해서 나온 횟수 사전에 정의
    for ar in range(len(array)):
        R_dict = dict()
        for r in array[ar]:
            if r != 0:
                if r in R_dict:
                    R_dict[r] += 1
                elif r not in R_dict:
                    R_dict[r] = 1

        # 첫번째는 value 두번째는 key로 정렬 이거 꼭 알아두기
        R_dict = sorted(R_dict.items(), key=lambda x: (x[1], x[0]))

        temp = []
        for item in R_dict:
            x, y = item
            temp.append(x)
            temp.append(y)

        # 길이가 100개 넘어가면 처음 100개만 살린다
        if len(temp) > 101:
            array[ar] = temp[:101]

        else:
            array[ar] = temp

        length = max(length, len(temp))

    # 길이가 짧은 것들은 뒤에 0으로 채운다
    for item in array:
        if len(item) < length:
            item += [0]*(length-len(item))

    return None


def C_operation():

    global array

    # 얘도 알아두자 배열 transpose하는 방법
    array = list(zip(*array))

    # 열 연산 따로 정의하지 말고 전치행렬 구한다음에 열연산 하자
    R_operation()
    array = list(zip(*array))

    return None


for i in range(3):
    array.append(list(map(int, input().split())))

time = 0

# 100초 돌리기
while time < 101:

    R = len(array)  # 행
    C = len(array[0])  # 열

    # 원하는 index에 값이 오면 break
    if r-1 < R and c-1 < C:
        if array[r-1][c-1] == k:
            print(time)
            break

    if R >= C:
        R_operation()

    else:
        C_operation()

    time += 1

    if time == 101:
        print(-1)
