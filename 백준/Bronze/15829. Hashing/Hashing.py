N = int(input())
lst = [ord(i) - 96 for i in list(map(str, input()))]

po = 0
hash = 0
for num in lst:
    hash += num * (31 ** po)
    po += 1
if hash >= 1234567891:
    print(round(hash%1234567891))
else:
    print(hash)