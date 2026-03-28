N, k = map(int, input().split())
lst = list(map(int, input().split()))

lst = sorted(lst, reverse=True)
print(lst[k-1])