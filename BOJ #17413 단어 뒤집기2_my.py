import sys
line = sys.stdin.readline().rstrip()
answer = ""
temp = ""
check = False

for i in range(len(line)):
    if line[i] != " " and line[i] != "<":
        temp += line[i]

    if line[i] == "<":
        if temp:
            answer += temp[::-1]
        answer += "<"
        temp = ""
        check = True
    elif line[i] == ">":
        check = False
        answer += temp
        temp = ""
    elif line[i] == " " or i == len(line)-1:
        if check == False:
            temp = temp[::-1]
        answer += temp + " "
        temp = ""
    
print(answer.rstrip())
