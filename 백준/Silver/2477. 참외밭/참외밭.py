W = []
H = []
Total = []
small =[]
num = int(input())

for i in range(6) :
    a,b = map(int,input().split())
    Total.append([a,b])
    if a == 1 or a == 2 :
        W.append(b)
        
    if a == 3 or a == 4 :
        H.append(b)
        
        
for i in range(6) :
    if max(W) == Total[i][1] and max(H) == Total[(i-1)%6][1]:
        small.append(Total[(i+2)%6][1])
        small.append(Total[(i+3)%6][1])
        
    elif max(W) == Total[i][1] and max(H) == Total[(i+1)%6][1]:
        small.append(Total[(i+4)%6][1])
        small.append(Total[(i+3)%6][1])


               
print((max(W)*max(H) - small[0]*small[1])*num) 