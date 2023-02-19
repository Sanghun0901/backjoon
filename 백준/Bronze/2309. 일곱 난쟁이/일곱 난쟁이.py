a = []
count = 0
while count < 9 :
    b=int(input())
    count += 1
    a.append(b)

a.sort(reverse=False)
d = sum(a) - 100
y = []
for i in range(9) :
    for j in range(i+1,9) :
        if a[i] + a[j]== d :
            x = a[i]
            z = a[j]
            y.append(x)
            y.append(z)
            if sum(list(set(a) - set(y))) == 100:
                g= list(set(a) - set(y))
                break

g.sort()
for i in g :
    print(i)