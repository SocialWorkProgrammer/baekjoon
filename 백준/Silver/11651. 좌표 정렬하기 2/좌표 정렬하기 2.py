N = int(input())
lst = []
for tc in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])

for a, b in sorted(lst, key = lambda x:(x[1], x[0])):
    print(a, b)
