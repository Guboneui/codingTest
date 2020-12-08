def solution(n):
    k = []
    n = str(n)
    for i in range(len(n)):
        k.append(n[i])

    return list(map(int, k[::-1]))