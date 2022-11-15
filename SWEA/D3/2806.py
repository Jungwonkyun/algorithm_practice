TC = int(input())


def solve(Queen, N, row):
    count = 0
    # 끝까지 간 경우에만 return 값을 줘서 count 올려준다
    if N == row:
        return 1

    # 세로 하나씩 배치
    for col in range(N):
        Queen[row] = col
        for r in range(row):
            # 만약 열이 겹치는 경우에 break
            if Queen[r] == col:
                break
            # 대각선 열에 있을 경우 break
            if abs(Queen[row]-Queen[r]) == abs(row-r):
                break
        # for-else 구문 break에 안 걸러지는 경우만
        else:
            count += solve(Queen, N, row+1)

    return count


for t in range(1, TC+1):
    N = int(input())
    Queen = [0]*N
    print("#{} {}".format(t, solve(Queen, N, 0)))
