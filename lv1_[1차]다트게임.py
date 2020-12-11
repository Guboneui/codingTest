def solution(dartResult):
    score = []
    n = ''
    for i in dartResult:
        #if i.isnumeric():
            #n += i
        if i.isdigit():
            n += i
        elif i == 'S':
            score.append(int(n) ** 1)
            n = ''
        elif i == 'D':
            score.append(int(n) ** 2)
            n = ''
        elif i == 'T':
            score.append(int(n) ** 3)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2
        elif i == '#':
            score[-1] *= -1
    return sum(score)




"""
dartResult = "10D2S#10S"

k = list(dartResult)
print(k)
a = []
"""
"""
if (k[0]).isdigit() == True and (k[1]).isdigit() == True:
    print(int(k[0] + k[1]))
else:
    print(1)
"""


"""
for i in range(len(k)):
    if k[i].isdigit() == True and k[i+1].isdigit() == True:
        a.append((k[i] + k[i+1]))
        i += 1
    elif i>0 and k[i-1].isdigit() == True and k[i].isdigit() == True:
        pass
    else:
        a.append(k[i])

print(a)

aa = []

result = []

if a[0].isdigit == True:

    aa.append(a[0])
print(aa)
"""
"""
for i in range(len(a)-2):
    num = ''
    if a[i].isdigit == True:
        num += a[i]
        if a[i+1] == 'S':
            num = int(num) ** 1
            result.append(num)
            if a[i+2] == '*':
                result.append(a[i+2])
            elif a[i+2] == '#':
                result.append(a[i+2])


        elif a[i+1] == 'D':
            num = int(num) ** 2
            result.append(num)
            if a[i + 2] == '*':
                result.append(a[i+2])
            elif a[i + 2] == '#':
                result.append(a[i+2])



        elif a[i+1] == 'T':
            num = int(num) ** 3
            result.append(num)
            if a[i+2] == '*':
                result.append(a[i+2])
            elif a[i+2] == '#':
                result.append(a[i+2])



print(result)
"""
