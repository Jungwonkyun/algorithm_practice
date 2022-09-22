number = set(range(1,10001))
num_set = set()

for num in range(1,10001):
    
    temp = num
    str_num = str(num)
    
    for i in range(len(str_num)):
        temp += int(str_num[i])

    num_set.add(temp)
    temp = 0 

new_set = number - num_set
new_set = list(new_set) 
new_set.sort()

for i in range(len(new_set)):
    print(new_set[i])

