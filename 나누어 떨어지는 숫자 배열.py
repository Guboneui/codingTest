def solution(arr, divisor):
    k = []
    for i in range(len(arr)):
        if(arr[i] %divisor) == 0:
            k.append(arr[i])
    if len(k) ==0:
        k.append(-1)
    return sorted(k)