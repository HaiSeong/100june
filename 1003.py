
dp = dict()

dp[0] = (1,0)
dp[1] = (0,1)

def fibonacci(n):
    if n == 0:
        return dp[0]
    elif n==1:
        return dp[1]
    else:
        if n-1 not in dp:
            dp[n-1] = fibonacci(n-1)
        num1 = (dp[n-1][0],dp[n-1][1])
        if n-2 not in dp:
            dp[n-2] = fibonacci(n-2)
        num2 = (dp[n-2][0],dp[n-2][1])

        return (num1[0]+num2[0],num1[1]+num2[1])



n = int(input())

for _ in range(n):
    temp = int(input())
    print("%d %d"%(fibonacci(temp)[0],fibonacci(temp)[1]))

