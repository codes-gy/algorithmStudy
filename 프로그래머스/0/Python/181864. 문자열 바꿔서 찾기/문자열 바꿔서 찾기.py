def solution(myString, pat):
    convertString = ''.join('B' if x == 'A' else 'A' for x in myString)
    return 1 if pat in convertString else 0