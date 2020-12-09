def solution(arr):
    arr = str(arr)
    kk = []
    for i in range(len(arr)):
        kk.append(int(arr[i]))

    return (True and (int(arr) % sum(kk) == 0) or False)
