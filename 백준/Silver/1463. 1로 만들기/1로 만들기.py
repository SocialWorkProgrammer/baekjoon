import sys
input = sys.stdin.readline


N = int(input())

'''def bottomup():
    lst = [0] * (N+1)
    for i in range(2, N+1):
        lst[i] = lst[i-1] + 1
        if i % 2 == 0:
            lst[i] = min(lst[i], lst[i // 2] + 1)
        elif i % 3 == 0:
            lst[i] = min(lst[i], lst[i // 3] + 1)
    return lst[-1]
print(bottomup())'''


memo = {1:0} # 1부터 시작, 1에서 더 연산할 필요가 없으므로 값이 0
def topdown(x):
    # print(x)
    if x in memo.keys():
        return memo[x]
    elif x % 2 == 0 and x % 3 == 0:
        memo[x] = min(topdown(x // 2)+1, topdown(x // 3)+1)
    elif x % 2 == 0:
        memo[x] = min(topdown(x // 2)+1, topdown(x - 1)+1)
    elif x % 3 == 0:
        memo[x] = min(topdown(x // 3)+1, topdown(x - 1)+1)
    else:
        memo[x] = topdown(x-1) + 1
    return memo[x]
print(topdown(N))