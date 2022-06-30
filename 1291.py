# // 연산자 꼭 주의 !!!


is_e = 0
is_im = 0

n = int(input())

if n == 4 or n >= 6:
    n_cpy = n
    sum = 0
    while n_cpy>0:
        sum+= n_cpy%10
        n_cpy//=10
    if sum %2 == 1:
        is_e = 1

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return 0

    return 1

cnt = 0
for i in range(2,n+1):
    if is_prime(i) == 1:
        if n % i == 0:
            cnt+=1

if n == 2 or n == 4 or cnt == 2:
    is_im = 1

if is_e == 1 and is_im == 1:
    print(4)
elif is_e == 1:
    print(1)
elif is_im == 1:
    print(2)
else:
    print(3)