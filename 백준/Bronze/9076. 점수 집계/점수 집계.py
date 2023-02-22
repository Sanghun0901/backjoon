c = int(input())
b = []

for _ in range(0,c) :
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    a.pop(0)
    a.sort(reverse = False)
    a.pop(0)
    if (a[2] - a[0]) >= 4 :
        a = 'KIN'
        b.append(a)
        
    else :
        a =sum(a)
        b.append(a)

for i in b:
    print(i)