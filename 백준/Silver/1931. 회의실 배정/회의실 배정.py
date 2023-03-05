num = int(input())
task = []
for _ in range(num) :
    nums = list(map(int,input().split()))
    task.append(nums)
    
task.sort(key = lambda x : (x[1],x[0]))

cnt = 1
end = task[0][1]
for i in range(1, num) :
    if end <= task[i][0] :
        end = task[i][1]
        cnt += 1
        
print(cnt)