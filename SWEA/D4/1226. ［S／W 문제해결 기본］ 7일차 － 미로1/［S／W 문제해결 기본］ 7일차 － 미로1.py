from collections import deque

for _ in range(10):
    t = int(input())
    N = 16                                         
    arr = [list(map(int, input())) for _ in range(N)]     
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]     
    visit = deque([])
    stack = deque([])
    res = 0

    for i in range(N):
        for j in range(N):                
            if arr[i][j] == 2:            
                stack.append((i, j))       

       
    while stack:               
        cordinate = stack.popleft()
        ix, iy = cordinate[0], cordinate[1]  
        for x, y in delta:     
            dx = ix + x
            dy = iy + y
            if 0 <= dx < N and 0 <= dy < N:  
                if arr[dx][dy] == 0 and (dx, dy) not in visit:    
                    visit.append((dx, dy))
                    stack.append((dx, dy))  
                elif arr[dx][dy] == 3:
                    res = 1   
                    break
        if res:
            break

    print(f'#{t} {res}')
