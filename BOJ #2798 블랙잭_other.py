import sys

def black(n, m, c):
  answer = set()
  for i in range(n-2):
    for j in range(i+1, n-1):
      for k in range(j+1, n):
        p = c[i] + c[j] + c[k]
        if p <= m:
          answer.add(p)
          break
  return max(answer)

print(black(*map(int, sys.stdin.readline().split()), sorted(map(int, sys.stdin.readline().split()), reverse = True)))
