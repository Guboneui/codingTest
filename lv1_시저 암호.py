def solution(s,n):
    k = []
    s = list(s)
    kk = 0
    for i in range(len(s)):
        if ord(s[i]) ==32:
            k.append(" ")
        elif (ord(s[i])>=65 and ord(s[i])<=90): #대문자일 경우
            kk = ord(s[i]) + n
            if kk>90:
                kk -= 26
            k.append(chr(kk))
        elif (ord(s[i])>=97 and ord(s[i])<=122):
            kk = ord(s[i]) + n
            if kk>122:
                kk -= 26
            k.append(chr(kk))
    return ("".join(k))

#아스키 코드 값을 이용하여