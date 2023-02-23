N,L,H = map(int,input().split())
    
def up(x) :
    return x<=100
S = list(filter(up,list(map(int,input().split()))))

S.sort(reverse = True)
for _ in range(H):
    S.pop(0)

S.sort(reverse = False)
for _ in range(L):
    S.pop(0)

print(sum(S)/int(N-L-H))