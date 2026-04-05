S = input()
print(*[S.count(chr(i)) for i in range(ord('a'), ord('z')+1)])