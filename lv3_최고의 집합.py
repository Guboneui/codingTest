import math


def solution(n, s):
    if s < n:
        return [-1]
    k = []
    answr = 1
    for i in range(n):
        k.append(s / n)

    for i in range(s % n):
        k[i] = math.ceil(k[i])
    for i in range(s % n, len(k)):
        k[i] = math.floor(k[i])

    k.sort()
    return k