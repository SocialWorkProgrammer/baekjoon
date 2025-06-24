ascending = [i for i in range(1, 8+1)]
descending = [i for i in range(8, 0, -1)]

lst = list(map(int, input().split()))
if lst == ascending:
    print('ascending')
elif lst == descending:
    print('descending')
else:
    print('mixed')