# 숫자가 붙어있을 경우 map과 input()을 이용하면 쉽게 뗄 수 있다.
A = int(input())
B = list(map(int,input()))

print(A * B[-1])
print(A * B[-2])
print(A * B[0])
print(A * int(str(B[0]) + str(B[1]) + str(B[2])))