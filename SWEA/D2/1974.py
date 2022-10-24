
test_case = int(input())

for n in range(test_case):
    sudoku = []
    flag = 1
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))

    # 행확인
    for row in sudoku:
        row = sorted(row)
        if row != check:
            flag = 0
            break

    if flag == 0:
        print("#{} {}".format(n+1, 0))
        continue

    # 열확인
    for x in range(9):
        temp = []
        for y in range(9):
            temp.append(sudoku[y][x])
        temp = sorted(temp)
        if temp != check:
            flag = 0
            break

    if flag == 0:
        print("#{} {}".format(n+1, 0))
        continue

    # 사각격자 확인
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            temp = []
            start = sudoku[y][x]
            for i in range(0, 3):
                for j in range(0, 3):
                    temp.append(sudoku[y+i][x+j])

            temp = sorted(temp)
            if temp != check:
                flag = 0
                break

        if flag == 0:
            break

    print("#{} {}".format(n+1, flag))
