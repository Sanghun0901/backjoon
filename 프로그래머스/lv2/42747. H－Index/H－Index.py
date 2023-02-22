
2
3
4
5
6
7
8
9
10
11
12
def solution(citations):
    citations.sort(reverse=True)
    max_h = len(citations)

    for i in range(max_h, -1, -1):
        higher = sum(map(lambda n: n > i, citations))
        same = sum(map(lambda n: n == i, citations))
        if higher + same >= i:
            return i

    return 0