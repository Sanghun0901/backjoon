import queue

n, m = map(int, input().split())

q = queue.Queue()
pw_dict = {}

for i in range(n):
    site, pw = input().split()
    pw_dict[site] = pw

for i in range(m):
    q.put(input())

while not q.empty():
    site = q.get()
    print(pw_dict[site])