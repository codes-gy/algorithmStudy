def solution(myString):
    answer = [x for x in myString.split('x') if x]
    return sorted(answer)