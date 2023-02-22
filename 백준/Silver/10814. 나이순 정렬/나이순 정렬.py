a = int(input())
b=[]
for _ in range(a) :
    b.append(list(map(str,input().split())))
    
b.sort(key=lambda x:int(x[0]))  
    
for i in b :
    print(i[0],i[1])