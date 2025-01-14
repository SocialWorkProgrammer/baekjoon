N = int(input())
lst = []
for tc in range(N):
    lst.append(input().split()[0])

name_count = {}
for name in lst:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1
# print(name_count)

for i in list(name_count):
    if name_count[i] % 2 == 0:
        del name_count[i]

for j in sorted(name_count, reverse=True):
    print(j)