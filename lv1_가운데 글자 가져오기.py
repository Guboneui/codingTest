def solution(s):
    k = len(s)
    if((k%2) == 0):
        a = (k//2)
        return s[a-1 : a+1]
    else:
        a = (k//2)
        return s[a]