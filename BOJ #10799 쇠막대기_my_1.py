import sys
from collections import deque

dq = deque(sys.stdin.readline().rstrip())
prev = ""
cnt = 0
answer = 0

while dq:
    new = dq.popleft()
    if new == "(":
        cnt += 1
    elif new == ")":
        cnt -= 1
        if prev == "(":
            answer += cnt
        else:
            answer += 1
    prev = new
        
print(answer)