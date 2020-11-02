def solution(array, commands):
    k = []
    for i in range(len(commands)):
        kk = []
        kk = sorted(array[commands[i][0]-1 : commands[i][1]])
        k.append(kk[commands[i][2]-1])
    return k
