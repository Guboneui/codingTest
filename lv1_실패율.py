def solution(N, stages):
    k = len(stages)
    a = []

    for i in range(1, N + 1):
        a.append(stages.count(i) / k)
        k = k - stages.count(i)

        if k == 0:
            while (len(a) < N):
                a.append(0) # 아무도 통과 못한 경우 예외처리

            break

    result = []

    for i in range(len(a)):
        result.append(a.index(max(a)) + 1)
        a[a.index(max(a))] = -1

    return result