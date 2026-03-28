A, B, V = map(int, input().split())

if V <= A:
    print(1)
else:
    remain = (V-A) % (A-B)
    share = (V-A) // (A-B)
    if remain == 0:
        print(share + 1)
    else:
        print(share + 2)