def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()

    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]

    k = ["ICN"]
    result = []

    while k:
        top = k[-1]
        if top not in routes or len(routes[top]) == 0:
            result.append(k.pop())
        else:
            k.append(routes[top].pop())

    result.reverse()
    return result