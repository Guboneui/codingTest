def solution(n):
    cnt = 0

    if n == 1:
        return 0

    for i in range(500):
        if (n % 2 == 0):
            n = n // 2
        else:
            n = n * 3 + 1

        cnt += 1
        if n == 1:
            return cnt

    return -1