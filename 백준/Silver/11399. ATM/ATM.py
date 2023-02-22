a = int(input())
b = list(map(int,input().split()))
b.sort()
c = []

for i in range(1,a+1) :
    e = sum(b[0:i])
    c.append(e)
    
print(sum(c))