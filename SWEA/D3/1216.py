for t in range(1, 11):
    puzzle = []
    tc = int(input())
    for _ in range(100):
        puzzle.append(list(map(str, input())))

    result = 1

    for _ in range(2):
        for i in range(100):
            for j in range(100):
                for k in range(100, j-1, -1):
                    orig = "".join(puzzle[i][j:k])
                    rev = orig[::-1]
                    if orig == rev:
                        result = max(result, len(orig))
        puzzle = list(map(list, zip(*puzzle)))

    print("#{} {}".format(t, result))
