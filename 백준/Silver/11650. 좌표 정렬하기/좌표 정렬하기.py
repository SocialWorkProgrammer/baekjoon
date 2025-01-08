N = int(input())
lst = []
for tc in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])

for a, b in sorted(lst):
    print(a, b)