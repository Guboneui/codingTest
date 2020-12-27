"""효율성 실패
def solution(n, works):
    if sum(works) <= n:
        return 0

    for i in range(n):
        works[works.index(max(works))] = works[works.index(max(works))] - 1
    return sum([i**2 for i in works])
"""
import heapq  # 최소 힙 사용


def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-i for i in works]
    heapq.heapify(works)
    while n > 0:
        heapq.heappush(works, heapq.heappop(works) + 1)
        n -= 1
    return sum([i ** 2 for i in works])