def solution(progresses, speeds):
    check = []
    total = []
    for i in range(len(progresses)) :
        total.append(progresses[i] + speeds[i])
    a = len(total)
    cnt = 0
    while total :
        cnt = 0
        while total :
            if total[0] >= 100 :
                cnt+=1
                del total[0],progresses[0], speeds[0]
                a -=1
            else : break
        if cnt > 0 :
            check.append(cnt)
        for i in range(len(total)):
            total[i] = total[i] + speeds[i]

    return check