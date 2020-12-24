def solution(begin, target, words):
    if target not in words:
        return 0

    k = [begin]
    answer = 0

    while len(words) > 0:
        for i in k:
            temp = []
            for word in words:
                count = 0
                for j in range(len(begin)):
                    if i[j] != word[j]:
                        count += 1
                    if count == 2:
                        break
                if count == 1:
                    temp.append(word)
                    words.remove(word)
        answer += 1

        if target in temp:
            return answer
        else:
            k = temp


