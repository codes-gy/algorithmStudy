import math
def solution(num_list):
    mul = math.prod(num_list)
    sum_val = sum(num_list) ** 2
    return 1 if mul < sum_val else 0