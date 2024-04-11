num1 = ''
num2 = ''
A, B = input().split()
for i in range(1, 4):
    num1 += A[-i]
    num2 += B[-i]
if int(num1) > int(num2):
    print(num1)
else:
    print(num2)