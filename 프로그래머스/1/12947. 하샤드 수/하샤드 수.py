def solution(x):
    digit = sum([int(i) for i in str(x)])
    return x % digit == 0