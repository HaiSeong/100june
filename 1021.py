from collections import deque

n, m = map(int, input().split())

array = list(map(int, input().split()))

cnt = 0

deq = deque(range(1,n+1))

for a in array:
    take1 = 0
    deq_cpy = deque(deq)
    while deq_cpy[0] != a:
        deq_cpy.append(deq_cpy.popleft())
        take1+=1

    take2 = 0
    deq_cpy = deque(deq)
    while deq_cpy[0] != a:
        deq_cpy.appendleft(deq_cpy.pop())
        take2+=1

    if take1 < take2:
        while deq[0] != a:
            deq.append(deq.popleft())
        cnt+=take1
    else:
        while deq[0] != a:
            deq.appendleft(deq.pop())
        cnt+=take2

    deq.remove(a)

print(cnt)