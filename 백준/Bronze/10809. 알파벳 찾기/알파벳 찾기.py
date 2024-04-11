S = input()
a = [-1 for i in range(26)]
for i in S:
    a[ord(i)-97] = S.index(i)
print(*a)