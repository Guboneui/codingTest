def solution(n):
    k = [1, 2]
    if n == 1:
        return k[n - 1]
    elif n == 2:
        return k[n - 1]
    elif n >= 3:
        for i in range(3, n + 1):
            k.append(k[i - 3] + k[i - 2])
        return k[n - 1] % 1234567