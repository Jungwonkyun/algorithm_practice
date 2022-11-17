test_case = int(input())

for tc in range(1, test_case+1):
    string = input()
    flag = True
    card_list = [[] for _ in range(4)]
    for i in range(len(string)//3):
        shape = string[3*i]
        number = int(string[3*i+1:3*i+3])

        if shape == "S":
            if number in card_list[0]:
                flag = False
                break
            card_list[0].append(number)
        elif shape == "D":
            if number in card_list[1]:
                flag = False
                break
            card_list[1].append(number)
        elif shape == "H":
            if number in card_list[2]:
                flag = False
                break
            card_list[2].append(number)
        else:
            if number in card_list[3]:
                flag = False
                break
            card_list[3].append(number)

    if flag == False:
        print("#{} {}".format(tc, "ERROR"))

    else:
        print("#{} {} {} {} {}".format(
            tc, 13-len(card_list[0]), 13-len(card_list[1]), 13-len(card_list[2]), 13-len(card_list[3])))
