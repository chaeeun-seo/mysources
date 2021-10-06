import sys

arr = sys.stdin.readline().rstrip().replace(">", "*<").split("<")
answer = ""

for big in arr:
    if big[-1:] == "*":
        answer += "<" + big[:-1] + ">"
    else:
        small = big.split()
        answer += " ".join([word[::-1] for word in small])

print(answer)