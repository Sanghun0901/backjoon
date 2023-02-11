c = []
for i in range(5) :
    if len(c) < 5 :
        c.append(int(input()))
        
print(int(sum(c)/len(c)))
print(sorted(c)[2])