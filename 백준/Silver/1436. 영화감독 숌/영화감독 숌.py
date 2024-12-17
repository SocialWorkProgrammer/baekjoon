N = int(input())

anslst = []
M = '666'
a = 665
while True:
    a += 1
    if M in str(a):
        anslst.append(a)
        if len(anslst) == N:
            print(anslst[-1])
            break