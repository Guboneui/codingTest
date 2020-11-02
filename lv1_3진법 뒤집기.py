
"""num = '3212'  #5진법

base = 5

answer = int(num, base)

print(answer)       #10진수로 나타낸 값

#=>n진법으로 표기된 string을 10진법 숫자로 바꾸는 방법
"""


def solution(n):
    result = []

    while n > 0:
        n, r = divmod(n, 3)
        result.append(r)
    for i in range(len(result)):
        result[i] = str(result[i])
    s = ''.join(result)

    answer = int(s, 3)
    return answer