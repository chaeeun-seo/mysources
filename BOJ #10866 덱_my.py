import sys
from collections import deque

dq = deque()
n = int(sys.stdin.readline())
for i in range(n):
    command = sys.stdin.readline().rstrip()
    if command == "pop_front":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif command == "pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(dq))
    elif command == "empty":
        if dq: print(0)
        else: print(1)
    elif command == "front":
        if dq: print(dq[0])
        else: print(-1)
    elif command == "back":
        if dq: print(dq[-1])
        else: print(-1)
    elif command[:6] == "push_f":
        x = command.split()[1]
        dq.appendleft(x)
    elif command[:6] == "push_b":
        x = command.split()[1]
        dq.append(x)