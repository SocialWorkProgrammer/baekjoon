# 해결전략
# 세로로 읽으면 되므로, 빈 리스트에 반복문을 돌린 인풋 리스트들을 넣어 2차원 리스트로 만들고, 거기서 다시 한 번 반복문으로 돌려 값 빼오기

wordlst = []
word = ''
wordlen = []

for i in range(5):
    wordlst.append(list(input()))
    wordlen.append(len(wordlst[i]))
for j in range(max(wordlen)):
    for k in range(5):
        try:
            word += wordlst[k][j]
        except:
            pass
print(word)