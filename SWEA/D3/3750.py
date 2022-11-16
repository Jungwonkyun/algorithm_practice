T = int(input())
numbers = [input() for _ in range(T)]
results = []

for tc in range(T):
    number = numbers[tc]
    answer = 0
    while True:
        sum_num = 0
        for n in number:
            sum_num += int(n)

        if sum_num > 9:
            number = str(sum_num)
        else:
            answer = sum_num
            break
    results.append(answer)

for tc in range(T):
    print(f'#{tc+1} {results[tc]}')
