a = 5
b = 3
sum = 0

if a>b:
    a, b = b, a
for i in range(a, b+1):
    sum += i
print(sum)