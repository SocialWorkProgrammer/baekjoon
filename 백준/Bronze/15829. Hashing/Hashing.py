N = int(input())
lst = [ord(i) - 96 for i in list(map(str, input()))]

po = 0
hash = 0
for num in lst:
    hash += num * (31 ** po)
    po += 1
print(hash)