integer = int(input())
for i in range(integer):
    star = integer-i-1
    print(' ' * star + '*' * (2*i+1))
    if star == 0:
        break

for j in range(integer-1):
    star = j + 1
    print(' ' * star + '*' * (2*(integer-1)-(2*j+1)))