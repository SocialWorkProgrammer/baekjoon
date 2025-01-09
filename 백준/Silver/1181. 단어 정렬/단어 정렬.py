N = int(input())
wordlst = []
for tc in range(N):
    word = str(input())
    if word in wordlst:
        pass
    else:
        wordlst.append(word)
for i in sorted(wordlst, key = lambda x:(len(x), x)):
    print(i)