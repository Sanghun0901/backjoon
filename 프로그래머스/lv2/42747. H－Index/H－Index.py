def solution(citations):
    answer = 0
    for i in range(len(citations),-1,-1):
        def up(x) :
            return x>=i
        c = list(filter(up,citations))
        if len(c) <= i:
            answer = len(c)
            
        

    return answer