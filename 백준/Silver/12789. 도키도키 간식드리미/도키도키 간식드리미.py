import sys
from copy import deepcopy
N = int(input())
lst = list(map(int, input().split()))

cnt = 1
stack = []
lst2 = deepcopy(lst)
for i in lst:
    if i == cnt: # 대기줄에 해당 번호가 있을 경우
        lst2.remove(i)
        cnt += 1
        # print(f'대기줄에서 걸러진 번호 : {i}')
        if stack and stack[-1] == cnt: # 스택에 해당 번호가 있을 경우
            num = stack.pop()
            lst2.remove(num)
            cnt += 1
            # print(f'연속된 번호 : {num}')
            for i in stack[::-1]:
                if stack and i == cnt:
                    num = stack.pop()
                    lst2.remove(num)
                    cnt += 1
    else:
        stack.append(i) # 대기줄에 해당 번호가 없을 경우, 번호를 스택으로 옮김
        if stack[-1] == cnt:
            stack.pop()
            cnt += 1
for j in stack[::-1]:
    if j == cnt:
        stack.pop()
        cnt += 1

print('Nice' if not stack else 'Sad')