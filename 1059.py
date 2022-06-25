# 조합을 이용해 풀었다. 이번 학기 이산수학과 확렌프를 들어서 쉽게 풀수 있었다.
# nCr = n!/(r!*(n-r)!)

times = int(input())

for _ in range(times):
    n, m = map(int, input().split())

    fact1 = 1   # n!
    for i in range(2, m+1):
        fact1 *= i
    fact2 = 1   # r!
    for i in range(2, n+1):
        fact2 *= i
    fact3 = 1   # (n-r)!
    for i in range(2, m-n+1):
        fact3 *= i

    comb = fact1 // fact2 // fact3  #nCrR

    print(comb)
