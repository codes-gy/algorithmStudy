def solution(binomial):
    a, op, b = binomial.split(' ')
    a = int(a)
    b = int(b)
    
    match op:
        case '+': return a + b
        case '-': return a - b
        case '*': return a * b