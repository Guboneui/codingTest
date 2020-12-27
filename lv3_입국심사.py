def solution(n, times):
    answer = 0
    start = 1
    end = min(times) * n

    while start <= end:
        middle = (start + end) // 2
        k = n
        for i in times:
            k = k - (middle // i)
            if k <= 0:
                answer = middle
                end = middle - 1
        if k > 0:
            start = middle + 1

    return answer

