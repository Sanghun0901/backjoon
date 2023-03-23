from collections import deque
import heapq
import sys
num = int(sys.stdin.readline())
heap = []
for _ in range(num) :
    a=int(sys.stdin.readline())
    heapq.heappush(heap,-a)
    if a == 0 :
        print(-heapq.heappop(heap))