def solution(l, r):
    answer = []
    for x in range(l, r+1):
        str_x = str(x)
        is_valid = True
        for val in str_x:
            if val != '0' and val != '5':
                is_valid = False
                break
                
        if is_valid:
            answer.append(x)
            
    if not answer:
        return [-1]
    
    return answer