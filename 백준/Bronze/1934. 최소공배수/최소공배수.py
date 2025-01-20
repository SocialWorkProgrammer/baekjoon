T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    # Euclide 알고리즘
    def Euclidean(A, B):
        while B != 0:
            [A, B] = [B, A%B]
        return A
    GCD = Euclidean(A, B)
    print((A//GCD) * (B//GCD) * GCD)
