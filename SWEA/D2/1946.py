test_case = int(input())

for n in range(test_case):
    line = int(input())
    character_list = []
    for _ in range(line):
        char, iteration = map(str, input().split())
        iteration = int(iteration)
        temp = [char]*iteration
        character_list += temp

    print("#{}".format(n+1))
    for i in range(len(character_list)):
        if i % 10 == 0 and i != 0:
            print()
        print(character_list[i], end="")
