def solution(answer):
    check = []
    for i in range(len(answer)) :
        if i == 0 :
            check.append(answer[i])
        elif answer[i] != answer[i-1] :
            check.append(answer[i])

    return check