from collections import deque

test_case = int(input())


def beer_check():

    f_y, f_x = festival[0][0], festival[0][1]
    visited = []

    while check_point:

        possible = False
        y, x = check_point.popleft()

        if (abs(y-f_y)+abs(x-f_x) <= 1000):
            return "happy"

        else:
            for t_y, t_x in convini:
                if abs(y-t_y)+abs(x-t_x) <= 1000 and (t_y, t_x) not in visited:
                    check_point.append((t_y, t_x))
                    visited.append((t_y, t_x))
                    possible = True

    return "sad"


for i in range(test_case):
    check_point = deque()
    convini = []
    festival = []

    num_convini = int(input())
    x, y = map(int, input().split())
    check_point.append((y, x))

    for j in range(num_convini):
        x, y = map(int, input().split())
        convini.append((y, x))

    x, y = map(int, input().split())
    festival.append((y, x))

    print(beer_check())
