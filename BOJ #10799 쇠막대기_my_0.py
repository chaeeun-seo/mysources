import sys
from collections import deque

line = sys.stdin.readline().rstrip()
dq = deque(line)
stk = deque()
prev = ""
answer = 0

while dq:
    new = dq.popleft()
    if new == "(":
        stk.append(new)
    elif prev == "(" and new == ")":
        stk.pop()
        answer += len(stk)
    elif prev == ")" and new == ")":
        stk.pop()
        answer += 1
    prev = new
        
print(answer)