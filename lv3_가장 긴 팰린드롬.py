def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(1, len(s) + 1):
            if i <= j and s[i:j] == (s[i:j])[::-1]:
                if answer < len(s[i:j]):
                    answer = len(s[i:j])
    return answer
