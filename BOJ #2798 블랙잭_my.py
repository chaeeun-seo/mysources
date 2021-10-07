import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))
combi = list(combinations(cards, 3))
hap = [sum(x) for x in combi if sum(x) <= m]
print(max(hap))
