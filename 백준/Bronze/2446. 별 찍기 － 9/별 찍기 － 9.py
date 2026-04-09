N = int(input())
star = '*'
lst = [(2*(N-i)-1)*star for i in range(N)]
lst += reversed(lst)
lst.remove('*')

lst2 = [' ' * i for i in range(N)]
lst2 += reversed(lst2)
lst2.remove(' ' * (N-1))

for i in range(N*2-1):
    print(lst2[i] + lst[i])