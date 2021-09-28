import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
b = deque(range(1, n+1))
a = deque()
answer = []
cnt = 0

while b:
    limit = len(b)
    i = 0
    while i < limit:
        i += 1
        cnt += 1
        if cnt == k: 
            answer.append(str(b.popleft()))
            cnt = 0
        else: 
            a.append(b.popleft())
    b = a
    a = deque()

print("<", ", ".join(answer), ">", sep="")