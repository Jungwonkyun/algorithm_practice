#Code by 정원균 
#BaekJoon #1003

def fibonacci(num):

    DP = [[1, 0]]
    temp = [0, 0]

    for i in range(1, num+1):

        if i == 1:
            DP.append([0, 1])
            continue

        temp[0] = DP[i-1][0]+DP[i-2][0]
        temp[1] = DP[i-1][1]+DP[i-2][1]

        DP.append(temp)

        # 여기서 temp를 다시 initialize 안 해주면 reference가
        # 중복돼서 DP에 저장된 이전 값도 바꾼다.
        temp = [0, 0]

    return DP


def main():

    num_case = int(input())
    result = []

    for i in range(num_case):
        num = int(input())
        result.append(fibonacci(num)[-1])

        print(result[-1][0], result[-1][1])

    return None


main()
