Ulimlst = list(map(int, input().split()))
Startlst = list(map(int ,input().split()))

flag = 0
Ulim, Start = 0, 0
for i in range(9):
    Ulim += Ulimlst[i]
    if Ulim > Start:
        flag = 1
    Start += Startlst[i]
if flag == 1:
    print("Yes")
else:
    print("No")