def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    answer = set(answer)
    answer = list(answer)

    answer.sort()

    return answer



#from itertools import combinations
#def solution(numbers):
    #return sorted(list(set([sum(i, j]) for i , j in combinations(numbers, 2)])))
