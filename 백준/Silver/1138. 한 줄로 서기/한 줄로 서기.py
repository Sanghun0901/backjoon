n = int(input())
meter = list(map(int, input().split()))
ans = [0] * n
for idx in range(1, n+1):
    t = meter[idx-1]
    cnt = 0
    for i in range(n):
        if cnt == t and ans[i] == 0:
            ans[i] = idx
            break
        elif ans[i] == 0:
            cnt += 1
print(*ans)