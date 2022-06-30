
a,b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AnB = set(A).intersection(set(B))

result = set(A+B) - AnB

print(len(result))