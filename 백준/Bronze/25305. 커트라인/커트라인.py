d = []
a,b = map(int,input().split())
while True :
    if a > 0  and 1000 >= a:
        d.append(a)
    
        if b > 0 and a >= b : 
            d.append(b)
        break        
    
    else : 
        print('다시 입력해주세요')
        a,b = map(int,input().split())

    continue        

c = sorted(map(int,input().split()),reverse=True)
c = list(c)
while True :
    if c[-1] >= 0 and 10000 >= c[0]:
        if len(c) == a:
            print(c[b-1])
        break
    
    else :
        print('다시 입력해주세요')
        c = sorted(map(int,input().split()),reverse=True)
        c = list(c)

        continue    