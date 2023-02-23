def solution(array, commands):
    answer = []
    
    for i in commands :
        j=array[i[0]-1:]
        k=j[:i[1]-i[0]+1]
        k.sort()
        y=k[i[2]-1]
        answer.append(y)
    
    
    return answer