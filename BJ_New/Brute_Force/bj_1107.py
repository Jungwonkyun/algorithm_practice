target_channel = int(input())
fault = int(input())
channel_list = []
fault_list = []

def count_channel(fault_list,finish):

    new_num = 0
    #지금 채널에서 +,- 로만 이동
    minimum = abs(finish-100)
    
    #번호입력 & +,-을 통해 이동
    #500000인데 범위가 10000001로 잡은 이유는 채널은 무헌대 
    #500000보다 큰 범위에서 줄였을 때 더 적은 횟수를 기록할 수도 있다.
    for nums in range(1000001):
        nums = str(nums) 

        for i in range(len(nums)):
            if int(nums[i]) in fault_list:
                break 
            
            if i == len(nums)-1:           
                #두가지 횟수중에 작은 거 리턴
                minimum = min(minimum,abs(int(nums)-finish)+len(nums))

    return minimum

if fault != 0:
    fault_list = list(map(int,input().split())) 

print(count_channel(fault_list,target_channel))


