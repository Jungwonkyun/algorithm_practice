def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: 
            return False 
    return True


def prime(start,end):
    
    prime_list = [] 

    for i in range(start,end+1):

        if is_prime(i)==True:
            prime_list.append(i)

    return prime_list


def main():

    test_case = input().split()
    test_case[0] = int(test_case[0])
    test_case[1] = int(test_case[1])

    result = prime(test_case[0],test_case[1])    
    
    for i in range(len(result)):
        print(result[i])


    return None


main()