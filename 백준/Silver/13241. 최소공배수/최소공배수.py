A, B = map(int, input().split())
def Euclidean(a, b):
    while b != 0:
        [a, b] = [b, a % b]
    return a

GCD = Euclidean(A, B)
print(int((A // GCD) * (B // GCD) * GCD))