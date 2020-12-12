def solution(board, moves):
    new_board = []
    for i in range(len(board)):
        k = []
        for j in range(len(board)):
            k.append(board[j][i])
        new_board.append(k)

    box = []
    cnt = 0

    for i in moves:
        a = new_board[i - 1]
        for j in range(len(a)):
            if a[j] == 0:
                pass
            else:
                box.append(a[j])
                a[j] = 0
                break

        if len(box) > 1 and box[-1] == box[-2]:
            cnt += 2
            del box[-2:]
    return cnt