
def is_prime(n):
    if n <2:
        return 0
    for i in range(2,n):
        if n%i == 0:
            return 0

    return 1

def next_prime(n):
    temp = n+1
    while True:
        if is_prime(temp) == 1:
            return temp
        temp+=1


a, b = map(int, input().split())

under_prime_cnt = 0

for n in range(a, b+1):
    if is_prime(n) == 1:
        continue
    div = 2
    cnt = 0
    while n > 1:
        if n % div == 0:
            # print(n, div, cnt)
            n //= div
            cnt += 1
        else:
            # div = next_prime(div)
            div += 1

    if is_prime(cnt) == 1:
        under_prime_cnt+=1


print(under_prime_cnt)