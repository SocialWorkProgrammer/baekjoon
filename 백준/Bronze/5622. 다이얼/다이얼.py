words = input()
dial = ['0', '0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sums = 0
cnt = []
for word in words:
    for j in range(len(dial)):
        if word in dial[j]:
            sums += j
            break
print(sums)
