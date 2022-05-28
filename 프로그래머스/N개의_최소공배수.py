def solution(arr):
    answer = 0
    flag= True
    temp = 0
    
    while flag:
        temp +=1
        temp_1 = 0
        for value in arr:
            if temp % value == 0:
                temp_1 +=1
        if temp_1 == len(arr):
            flag = False
        
    return temp