def solution(s):

    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False

    # isdigit = 문자열이 숫자인지 판단
    # isalpha = 문자열이 문자인지 판단