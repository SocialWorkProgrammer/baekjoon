N = int(input())
M = list(input())
alpha = [input() for i in range(N)]
stack = []

for i in range(len(M)): # M의 원소 개수만큼 반복
    if M[i] not in '*/+-': # 피연산자라면
        stack.append(alpha[ord(M[i])-65]) # 추가해
    if M[i] in '*/+-':  # 연산자라면
        temp2 = float(stack.pop()) # temp 선언
        temp1 = float(stack.pop()) # 이때, 결과값이 소수점으로 나와야하므로 float 이용
        if M[i] == '+':
            stack.append(temp1 + temp2)
        if M[i] == '-':
            stack.append(temp1 - temp2)
        if M[i] == '*':
            stack.append(temp1 * temp2)
        if M[i] == '/':
            stack.append(temp1 / temp2)
a = "{:.2f}".format(stack[0])
print(a)