import sys
input = sys.stdin.readline

# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

N = int(input())
stack = []
for tc in range(N):
    lst = list(map(int, input().split()))
    if len(lst) == 2:
        a, b = lst[0], lst[1]
        stack.append(b)
    if len(lst) == 1:
        a = lst[0]
        if a == 2:
            if stack:
                top = stack.pop()
                print(top)
            else:
                print(-1)
        if a == 3:
            print(len(stack))
        if a == 4:
            if not stack:
                print(1)
            else:
                print(0)
        if a == 5:
            if stack:
                print(stack[-1])
            else:
                print(-1)