def solution(a, b):
    answer1 = int(f"{a}{b}")
    answer2 = int(f"{b}{a}")
    return max(answer1, answer2)