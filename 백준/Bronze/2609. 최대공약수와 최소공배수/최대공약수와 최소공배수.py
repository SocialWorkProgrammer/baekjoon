import sys
input = sys.stdin.readline

A, B = list(map(int, input().split()))

def ab(x):
    i = x
    setlst = set()
    while i >= 1:
        if x % i == 0:
            setlst.add(i)
        i -= 1
    return setlst
print(max(ab(A).intersection(ab(B))))

mul = A * B
setA = set()
setB = set()
for a in range(A,mul+1,A):
    setA.add(a)

for b in range(B, mul+1,B):
    setB.add(b)
print(min(setA.intersection(setB)))