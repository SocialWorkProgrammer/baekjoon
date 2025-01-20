a, b = map(int, input().split())
c, d = map(int, input().split())

def Euclidean(A, B):
    while B != 0:
        [A, B] = [B, A % B]
    return A
GCD = Euclidean(b, d)
LCM = ((b // GCD) * d)
numerator = (d//GCD * a + b//GCD * c)
denominator = LCM

fraction = Euclidean(numerator, denominator)
print(numerator // fraction)
print(denominator // fraction)