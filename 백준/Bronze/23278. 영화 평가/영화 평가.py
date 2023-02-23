N,L,H = map(int,input().split())
  
def up(x) :
    return x<=100
S1 = list(map(int,input().split()))
S = list(filter(up,S1))
if len(S) == N :
    S.sort(reverse = True)
    for _ in range(H):
        S.pop(0)

    S.sort(reverse = False)
    for _ in range(L):
        S.pop(0)

    print(sum(S)/int(N-L-H))
