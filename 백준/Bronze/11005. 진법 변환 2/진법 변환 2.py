import string
N, B = map(str, input().split())
N = int(N)
B = int(B)

formation = ''
if N < B:
    if N >= 10:
        formation += string.ascii_uppercase[N - 10]
    else:
        formation += str(N)
else:
    while N >= B:
        if N % B >= 10:
            formation += string.ascii_uppercase[N % B - 10]
        else:
            formation += str(N % B)
        N = N // B
        if N < B:
            if N >= 10:
                formation += string.ascii_uppercase[N - 10]
            else:
                formation += str(N)
            break
print(formation[::-1])