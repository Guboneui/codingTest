def solution(s):
    s = s.lower()

    return (True and (s.count("p") == s.count("y")) or False)