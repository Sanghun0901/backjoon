import sys

a = int(sys.stdin.readline())
c = []
for _ in range(0,a):
    c.append(int(sys.stdin.readline()))


for i in sorted(c) :
    print (i)