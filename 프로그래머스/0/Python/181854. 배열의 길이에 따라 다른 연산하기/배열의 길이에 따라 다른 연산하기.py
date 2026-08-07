def solution(arr, n):
    answer = []
    if len(arr) % 2 != 0:
        for x in range(0, len(arr), 2):
            arr[x] += n
    else:
        for x in range(1, len(arr), 2):
            arr[x] += n
    return arr