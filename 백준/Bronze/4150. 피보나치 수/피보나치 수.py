a= [1,1]
b = int(input())
for i in range(2,b) :
        b=a[i-1] + a[i-2]
        a.append(b)  

print(a[-1])    