def solution(answers):
    count = len(answers)
    a = [1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    result =[]
    total = [a,b,c]
    return_num = []
    for i in total :
        cnt = 0
        for j in range(count) :
            if answers[j] == i[:count][j] :
                cnt += 1
        result.append(cnt)
    if max(result) == 0 :
        return_num = []
    else: 
        if result.count(max(result)) == 3 :
            return_num = [1,2,3]

        if result.count(max(result)) == 2 :
            if max(result) == result[-1] and  max(result) == result[-2]:
                return_num = [result.index(max(result))+1,result.index(max(result))+2]
            elif max(result) == result[-1]:
                return_num = [result.index(max(result))+1,result.index(max(result))+3]  
            else:
                return_num = [result.index(max(result))+1,result.index(max(result))+2] 

        if result.count(max(result)) == 1 :
            return_num = [result.index(max(result))+1]
 
    return return_num