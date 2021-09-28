import sys

n, k = map(int, sys.stdin.readline().split())
l = list(range(1, n+1))
answer = []
i = 0

while l:
    i = (i + k - 1) % len(l)
    answer.append(str(l.pop(i)))

print("<", ", ".join(answer), ">", sep="")