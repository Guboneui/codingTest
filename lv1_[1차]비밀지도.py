def solution(n, arr1, arr2):
    arr1_bin = []
    arr2_bin = []

    result = []

    for i in range(len(arr1)):
        k = format(arr1[i], 'b')

        if len(k) < n:
            k1 = '0' * (n - len(k)) + k
            arr1_bin.append(k1)
        else:
            arr1_bin.append(k)

    for i in range(len(arr2)):
        kk = format(arr2[i], 'b')

        if len(kk) < n:
            k2 = '0' * (n - len(kk)) + kk
            arr2_bin.append(k2)
        else:
            arr2_bin.append(kk)

    for i in range(n):
        aaa = ""
        for j in range(n):
            if arr1_bin[i][j] == '0' and arr2_bin[i][j] == '0':
                aaa += " "
            else:
                aaa += "#"

        result.append(aaa)

    return result