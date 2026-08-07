def solution(seoul):
    answer = ''
    for x in range(len(seoul)):
        if seoul[x] == 'Kim':
            return f"김서방은 {x}에 있다"