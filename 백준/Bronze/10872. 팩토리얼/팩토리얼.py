def recursion(N):
    if N == 0:
        return 1
    return N * recursion(N-1)

print(recursion(int(input())))