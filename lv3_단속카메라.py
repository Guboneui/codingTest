def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    check = [False] * len(routes)

    camera = -30000
    answer = 0

    for i in range(len(routes)):
        if check[i]:
            continue
        answer += 1
        camera = routes[i][1]
        for j in range(i, len(routes)):
            if routes[j][0] <= camera <= routes[j][1]:
                check[j] = True
    return answer
