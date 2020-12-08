def solution(n):
    k = []
    for i in range(1, n+1):
        if n%i == 0:
            k.append(i)
    return sum(k)