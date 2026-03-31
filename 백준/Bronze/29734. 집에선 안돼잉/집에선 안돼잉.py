N, M = map(int, input().split())
T, sleep = map(int,input().split())

Zip = N + ((N-1)//8) * sleep
Dok = T + M + ((M-1)//8) * (2*T + sleep)
if Zip < Dok: print('Zip')
else: print('Dok')
print(min(Zip, Dok))