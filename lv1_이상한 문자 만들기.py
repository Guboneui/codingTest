def solution(s):
    s = s.lower()
    k = s.split(" ")

    kk = []

    for word in k:
        new_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        kk.append(new_word)

    return " ".join(kk)


"""
def solution(s):
    s = s.lower()
    k = s.split()           //split 차이점 중요
    
    kk = []
    
    
    for word in k:
        new_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        kk.append(new_word)
        
    return " ".join(kk)








"""