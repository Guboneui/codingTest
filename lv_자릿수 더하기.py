def solution(n):
    answer = 0


    k= str(n)
    for i in range(len(k)):
        answer += int(k[i])

    return answer