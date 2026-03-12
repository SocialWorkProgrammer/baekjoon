ISBN = list(map(str, input()))
sums = 0
x = 0
for i in range(len(ISBN)):
    n = ISBN[i]
    if i % 2 == 0:
        if n == '*':
            x = 1
            n = 0
        sums += int(n)
    elif i % 2 == 1:
        if n == '*':
            x = 3
            n = 0
        sums += 3 * int(n)
for i in range(10):
    if (sums + (x*i)) % 10 == 0:
        print(i)