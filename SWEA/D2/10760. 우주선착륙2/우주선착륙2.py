num = int(input())
for t in range(1, num+1):
    a, b = map(int, input().split())
    land = []
    for _ in range(a):
        land.append(list(map(int, input().split())))

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    check = 0
    for i in range(a):
        for j in range(b):
            cnt = 0
            test = land[i][j]
            for s in range(8):
                x = i
                y = j
                nx = x + dx[s]
                ny = y + dy[s]
                if nx < 0 or ny < 0 or nx >= a or ny >= b:
                    continue
                if land[nx][ny] < test:
                    cnt += 1
            if cnt >= 4:
                check += 1
    print(f"#{t} {check}")
