N, M = map(int, input().split())
sites = {}
for i in range(N):
    site, password = input().split()
    sites[site] = password

for j in range(M):
    memojang = input()
    if memojang in sites:
        print(sites[memojang])