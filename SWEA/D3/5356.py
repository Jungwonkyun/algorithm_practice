test_case = int(input())

for tc in range(1, test_case+1):
    string = []
    length = 0
    for i in range(5):
        temp = list(map(str, input()))
        length = max(length, len(temp))
        string.append(temp)

    for i in range(5):
        for j in range(length - len(string[i])):
            string[i].append("")

    new_string = ""

    for x in range(length):
        for y in range(5):
            new_string += string[y][x]

    print("#{} {}".format(tc, new_string))
