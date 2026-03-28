import sys, math
from itertools import combinations

n, k = list(map(int, input().split()))

def combination(n, k):
	return math.factorial(n) // (math.factorial(n-k) * math.factorial(k))

print(combination(n, k))