num = int(input())

fibodic = {1:1, 2:3}

def fibo(n):
    if n in fibodic:
        return fibodic[n]

    fibodic[n] = fibo(n-1) + n
    return fibodic[n]

n = 0
while True:
    n += 1
    if num <= fibo(n):
        share = n
        remainder = fibo(n) - num
        break
anslst = [i for i in range(1, share+1)]
if share % 2 == 1:
    ans = str(anslst[remainder]) + '/' + str(anslst[-remainder-1])
else:
    ans = str(anslst[-remainder-1]) + '/' + str(anslst[remainder])
print(ans)