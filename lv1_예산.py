def solution(d, budget):
    answer = 0
    # new_d = sorted(d)
    d.sort()
    for i in d:
        budget = budget - i
        if budget >= 0:
            answer += 1
        elif budget < 0:
            break

    return answer