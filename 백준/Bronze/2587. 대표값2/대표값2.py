lst = []
for tc in range(5):
    lst.append(int(input()))

for i in range(4, 0 , -1):
    for j in range(i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(int(sum(lst)/5))
print(lst[2])
