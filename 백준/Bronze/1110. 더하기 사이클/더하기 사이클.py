import sys
input = sys.stdin.readline


M = int(input())
N = M
cycles = 0

def smallerthan10(N):
    N = int(N) % 10
    return int(2 * str(N))

def largerthan10(N):
    N = str(N)
    i, j = map(int, N)
    k = int(str(i + j)) % 10
    return int(str(j) + str(k))

if int(N) < 10:
    N = smallerthan10(N)
else:
    N = largerthan10(N)
cycles += 1

while N != M:
    # print(f'N = {N}, M = {M}')
    if int(N) < 10:
        N = smallerthan10(N)
    else:
        N = largerthan10(N)
    cycles += 1
print(cycles)