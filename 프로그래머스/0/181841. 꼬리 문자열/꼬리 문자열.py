def solution(str_list, ex):
    answer = ''
    
    for val in str_list:
        if ex not in val:
            answer += val
    return answer