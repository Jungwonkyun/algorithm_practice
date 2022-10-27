test_case = int(input())

for n in range(test_case):
    money_count = []
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money = input()
    length = len(money)
    money = int(money)
    new_money = 0

    for i in range(len(money_list)):
        temp = money//money_list[i]
        new_money += money_list[i]*temp
        money -= money_list[i]*temp
        money_count.append(temp)

    print("#{}".format(n+1))
    for cnt in money_count:
        print(cnt, end=" ")
    print()
