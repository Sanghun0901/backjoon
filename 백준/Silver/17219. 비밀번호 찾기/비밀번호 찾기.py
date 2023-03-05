import queue
num, ber = map(int, input().split())
save = {}
q = queue.deque([])
for i in range(num):
    site, pw = input().split()
    save[site] = pw

find = []

for i in range(ber):
    site = input().strip()
    q.append(site)

while q:
    site = q.popleft()
    if site in save:
        find.append(save[site])

for pw in find:
    print(pw)