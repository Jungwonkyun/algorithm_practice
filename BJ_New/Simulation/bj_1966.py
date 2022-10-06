from collections import deque

test_case = int(input())

for i in range(test_case):
    printer = deque()
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))

    for i in range(len(paper)):
        # 우리가 알고싶은 문서라면 True 태그를 달아준다
        if i == M:
            printer.append((paper[i], True))

        # 우리가 알고싶은 문서가 아니라면 False 태그를 달아준다
        else:
            printer.append((paper[i], False))

    cnt = 1
    while printer:
        maximum = max(paper)
        priority, check = printer.popleft()

        # prior가 제일 높고 우리가 알고싶은 문서
        if priority == maximum and check == True:
            print(cnt)
            break

        # prior가 제일 높지만 우리가 알고싶은 문서는 아님
        elif priority == maximum and check == False:
            paper.remove(maximum)
            cnt += 1

        # prior가 제일 높지 않음
        elif priority < maximum:
            printer.append((priority, check))
