
def make_one(num):

    DP = [0]*(num+1)  # DP array

    for i in range(2, num+1):

        DP[i] = DP[i-1]+1

        # 현재 DP[i]와 DP[i//3]중 더 작은 값으로 업데이트
        if i % 3 == 0:
            DP[i] = min(DP[i//3]+1, DP[i])

        # 현재 DP[i]와 DP[i//2]중 더 작은 값으로 업데이트
        if i % 2 == 0:
            DP[i] = min(DP[i//2]+1, DP[i])

    return DP


def main():

    num = int(input())

    print(make_one(num)[num])

    return None


main()
