T = int(input())
st = []
for i in range(T):
    age, name = input().split()
    st.append([int(age), name])
for i in sorted(st, key= lambda st:st[0]):
    print(i[0], i[1])