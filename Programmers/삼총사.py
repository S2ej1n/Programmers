#3명의 정수 번호를 더했을 때 0이되면 삼총사.

def solution(number):
    subset = [[]]
    new_sub = []
    
    sum_res = 0
    count = 0
    
    for i in number:
        for j in range(len(subset)):
            subset.append(subset[j] + [i])
            
    for i in range(len(subset)):
        if len(subset[i]) == 3:
            new_sub.append(subset[i])
    
    for i in new_sub:
        for j in i:
            sum_res +=  j
        
        if sum_res == 0:
            count += 1
        
        sum_res = 0
    
    return count