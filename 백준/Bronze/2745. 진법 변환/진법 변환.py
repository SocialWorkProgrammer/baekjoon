N, B = map(str, input().split())
ans = 0
for i in range(len(N)):
    if ord(N[-1-i]) >= ord('A'):
        ans += int(B) ** i * (ord(N[-1-i])-55)
    else:
        ans += int(B) ** i * int(N[-1-i])
print(ans)