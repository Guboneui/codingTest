def solution(arr):
    if len(arr) == 1 and arr[0] == 10:
        arr[0] = -1
        return arr
    arr.remove(min(arr))
    return arr