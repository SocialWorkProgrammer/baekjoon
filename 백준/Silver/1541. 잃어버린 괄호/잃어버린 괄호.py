import sys, re
input = sys.stdin.readline

string = input()
lst = list(map(int, re.split(r'[+-]',string)))
ops = list(map(str, re.findall(r'[+-]', string)))

numlst = [lst[0]]
for i in range(len(ops)):
    if ops[i] == '-':
        numlst.append(lst[i+1])
    elif ops[i] == '+':
        numlst[-1] += lst[i+1]

ans = numlst[0]
if len(numlst) >= 2:
    for i in numlst[1:]:
        ans -= i
print(ans)