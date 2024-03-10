sugarpack = int(input())
cnt = 0
while sugarpack >= 0:
    if sugarpack <= 0:
        break
    if sugarpack % 5 == 0:
        sugarpack -= 5
        cnt += 1
    elif sugarpack % 5 != 0:
        sugarpack -= 3
        cnt += 1
if sugarpack != 0:
    print(-1)
else:
    print(cnt)
