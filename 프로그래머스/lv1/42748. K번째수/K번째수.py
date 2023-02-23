def solution(array, commands):
    answer = []
    
    for i in commands :
        b=array[i[0]-1:]
        t=b[:i[1]-i[0]+1]
        t.sort()
        y=t[i[2]-1]
        answer.append(y)
    
    
    return answer