# 초등학교 수학을 요하는 문제
# 3 % 4 => 빌려오기 => 30 % 4 = 7...2
# 2 % 4 => 빌려오기 => 20 % 4 = 5...0


a, b ,n = map(int, input().split())

a%=b

for i in range(n-1):
    a = (a*10) % b

print((a*10) // b)