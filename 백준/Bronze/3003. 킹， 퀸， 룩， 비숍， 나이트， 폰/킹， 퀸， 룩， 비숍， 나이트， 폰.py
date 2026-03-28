X = list(map(int, input().split()))
Y = [1, 1, 2, 2, 2, 8]
for i in range(len(X)):
    if X[i] != Y[i]:
        X[i] = Y[i] - X[i]
    elif X[i] == Y[i]:
        X[i] = 0
print(*X)