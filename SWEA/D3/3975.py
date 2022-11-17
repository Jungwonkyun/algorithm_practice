test_case = int(input())
answer = []

for _ in range(test_case):
    A, B, C, D = map(int, input().split())
    r1 = A/B
    r2 = C/D

    if r1 > r2:
        answer.append("ALICE")
    elif r1 < r2:
        answer.append("BOB")
    else:
        answer.append("DRAW")

for i in range(len(answer)):
    print("#{} {}".format(i+1, answer[i]))
