num = int(input())
nums =[num]
dp = [0]*1000001
report = ['' for i in range(num+1)]
report[1] = '1'


if num > 1 :
    for i in range(2,num+1) :
        dp[i] = dp[i-1] +1
        prev = i-1
        if i%3 == 0 and dp[i//3]+1 < dp[i]:
            dp[i] = min(dp[i],dp[i//3]+1)
            prev = i//3          
        if i%2 == 0 and dp[i//2]+1 < dp[i]:
            dp[i] = min(dp[i],dp[i//2]+1)
            prev = i//2
        report[i] = str(i) + " " + report[prev]
print(dp[num])
print(report[num])