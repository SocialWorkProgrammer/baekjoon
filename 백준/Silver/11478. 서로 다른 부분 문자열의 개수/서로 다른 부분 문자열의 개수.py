S = str(input())

# 1. lst로 풀기
# lst = []
# for i in range(len(S)):
#     for j in range(len(S)):
#         lst.append(S[i:j+1 ])
# print(len(set(lst))-1)

# 2. set으로 풀기
Sset = set()
for i in range(len(S)):
    for j in range(i+1):
        Sset.add(S[j:i+1])
print(len(Sset))