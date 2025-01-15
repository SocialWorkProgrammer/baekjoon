N, M = map(int, input().split())

pokedict = {input() : tc + 1 for tc in range(N)}
reverse_pokedict = {value : key for key, value in pokedict.items()}

problemlst = [input() for tc in range(M)]

for problem in problemlst:
    if problem in pokedict:
        print(pokedict[problem])
    else:
        print(reverse_pokedict[int(problem)])
