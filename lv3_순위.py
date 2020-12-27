def solution(n, results):
    win = dict()
    lose = dict()

    for i in range(1, n + 1):
        win[i] = set()
        lose[i] = set()

    for i in range(1, n + 1):
        for result in results:
            if result[0] == i:
                win[i].add(result[1])
            elif result[1] == i:
                lose[i].add(result[0])

        for winner in lose[i]:
            win[winner].update(win[i])
        for loser in win[i]:
            lose[loser].update(lose[i])

    answer = 0
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer