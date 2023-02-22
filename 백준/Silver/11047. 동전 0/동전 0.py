a,b = map(int,input().split())
c = []
for i in range(0,a) :
    d=int(input())
    if d == 1 :
        c.append(1)
    elif d%c[i-1] == 0 :
        c.append(d)
    else :
        while True :
            print('다시 입력하세요')
            d = int(input())
            if d%c[i-1] ==0:
                c.append(d)
                break

                
c.sort(reverse = True)
count = 0
for i in c :
    if b%i != b:
        f=b//i
        b = b%i
        count +=f
    else : continue
    
print(count)