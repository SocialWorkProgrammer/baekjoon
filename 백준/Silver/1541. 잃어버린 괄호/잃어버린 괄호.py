import sys, re
input = sys.stdin.readline

# 첫 '-' 이후의 수들은 모두 더한 뒤 한 번에 빼면 식의 최솟값이 됩니다!
# ex : 10-20+30-40의 경우, [10, 50, 40]으로 만든 후, 10-50-40으로 계산

string = input()
# 식에서 숫자만 추출
lst = list(map(int, re.split(r'[+-]', string)))
# 식에서 연산자만 추출
ops = list(map(str, re.findall(r'[+-]', string)))

# 첫 번째 숫자는 무조건 첫 묶음에 들어가므로 미리 넣어 둔다
numlst = [lst[0]]
for i in range(len(ops)): # 연산자를 기준으로 다음 숫자를 처리
    if ops[i] == '-': # '-'를 만나면 새로운 묶음을 시작
        numlst.append(lst[i+1])
    elif ops[i] == '+': # '+'는 현재 묶음에 더해 주기
        numlst[-1] += lst[i+1]

# 첫 묶음을 기준값으로 두고, 이후 묶음들을 차례로 빼기!
ans = numlst[0] # + 연산자만 나왔을 때 묶음이 한 개만 있으므로 ans에 numlst[0] 저장
if len(numlst) >= 2:
    for i in numlst[1:]:
        ans -= i
print(ans)