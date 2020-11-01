def solution(answers):
    k = [0, 0, 0]
    kk = []

    s11 = [1, 2, 3, 4, 5] * 2000
    s22 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    s33 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    for i in range(len(answers)):
        if answers[i] == s11[i]:
            k[0] += 1
        if answers[i] == s22[i]:
            k[1] += 1
        if answers[i] == s33[i]:
            k[2] += 1

    for i in range(3):
        if k[i] == max(k):
            kk.append(i+1)

    return kk
