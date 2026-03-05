caldict = {1:31, 2:28, 3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
date = ['SUN','MON','TUE','WED','THU','FRI','SAT']

x, y = list(map(int, input().split()))
cnt = 0
for i in caldict:
    if i == x:
        cnt += y
        break
    else:
        cnt += caldict[i]
print(date[cnt%7])