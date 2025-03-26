N = int(input())
A = list(map(int,input().split()))

lst = [0]

def binary_search(num): # num = A[i]
    s = 0
    e = len(lst)-1
    while s <= e:
        mid = s + (e-s)//2
        if lst[mid] < num:
            s = mid + 1
        else:
            e = mid -1
    return s

for i in range(N):
    if A[i] > lst[-1]:
        lst.append(A[i])
    else:
        lst[binary_search(A[i])] = A[i]
print(len(lst)-1)