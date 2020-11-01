numbers = [2, 1, 3, 4, 1]
num = 0
k = []

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        k.append(numbers[i] + numbers[j])

k = set(k)
k = list(k)


k.sort()
print(k)

