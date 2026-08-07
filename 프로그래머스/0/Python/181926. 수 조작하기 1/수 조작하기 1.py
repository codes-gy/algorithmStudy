def solution(n, control):
    
    for val in control :
        if val == 'w' :
            n += 1
        if val == 's' :
            n -= 1
        if val == 'd' :
            n += 10
        if val == 'a' :
            n -= 10
    return n