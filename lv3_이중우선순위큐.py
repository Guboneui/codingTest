def solution(operations):
    k = []
    a = []
    for i in range(len(operations)):
        if operations[i][0] == "I":
            operations[i] = operations[i].replace("I", "")
            k.append(int(operations[i]))

        elif operations[i][0] == "D":
            operations[i] = operations[i].replace("D", "")
            if len(k) == 0:
                pass
            elif int(operations[i]) == 1:
                k.remove(max(k))
            elif int(operations[i]) == -1:
                k.remove(min(k))

    if len(k) == 0:
        return [0, 0]
    else:
        a.append(max(k))
        a.append(min(k))
        return a
