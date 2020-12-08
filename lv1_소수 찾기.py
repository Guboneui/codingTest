#에라토스테네스의 체 사용하기

def solution(n):
    num = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in num:
            num -= set(range(i * 2, n + 1, i)) #set연산을 통해 제거 가능

    return len(num)