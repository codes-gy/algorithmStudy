def solution(n):
    if n % 2 != 0 : # n 이 홀수인 경우
        # 1부터 n까지 2씩 더해가며 증가(홀수)
        return sum(range(1, n + 1, 2))
    else : # n 이 짝수인 경우
        # 짝수를 제곱 연산 후 합을 구함
        return sum(i ** 2 for i in range(2, n + 1, 2))