num= int(input())
a= []
[a.append(list(map(int,input().split()))) for i in range(2)]
list1 = a[0]
list2 = a[1]

list1.sort()
list2.sort(reverse = True)

product = [x*y for x,y in zip(list1,list2)]

print(sum(product))