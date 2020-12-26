def solution(n):
    result = 0
    k = []
    k.append(1)
    k.append(2)

    for i in range(2, n):
        k.append((k[-1] + k[-2]) % 1000000007)

    return k[-1]