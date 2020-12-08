def solution(n):
    k = sorted(list(map(str, (str(n)))))
    k.reverse()
    a = ""
    for i in range(len(k)):
        a += k[i]

    return int(a)
