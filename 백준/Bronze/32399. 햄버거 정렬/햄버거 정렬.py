S = input()
if S == '(1)':
    print(0)
elif S == ')1(':
    print(2)
else:
    print(1)
# 모든 가능한 경우의 수
# (1) = 0
# ()1 = 1
# 1() = 1
# 1)( = 1
# )(1 = 1
# )1( = 2