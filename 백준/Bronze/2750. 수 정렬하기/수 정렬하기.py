N = int(input())
cnt = 0
lst = []
for tc in range(N):
    lst.append(int(input()))
while True:
    print(min(lst))
    lst.remove(min(lst))
    if lst == []:
        break