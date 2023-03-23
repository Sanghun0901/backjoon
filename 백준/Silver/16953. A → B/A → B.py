start, final = map(str,input().split())
final = list(final)
cnt = 0
while True :
    if ''.join(final) == start :
        print(cnt +1)
        break 
    else:
        num  = final.pop()
        if any(num == i for i in ['3','5','7','9']) :
            print(-1)
            break
        else:
            if num == '1' :
                cnt += 1
                if len(final) == 0 :
                    print(-1)
                    break
            if any(num == i for i in ['2','4','6','8','0']) :
                final.append(num)
                final = list(str(int(''.join(final))//2))
                cnt +=1
                if len(final) == 0 :
                    print(-1)
                    break