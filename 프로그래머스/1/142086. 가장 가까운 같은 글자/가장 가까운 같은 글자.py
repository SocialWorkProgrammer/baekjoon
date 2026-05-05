def solution(s):
    answer = []
    sdict = {}
    sl = {}
    for i, c in enumerate(s):
        sdict[c] = i
        if c not in sl.keys():
            answer.append(-1)
            sl.update({c:i})
        else:
            answer.append(i-sl[c])
            sl.update({c:i})
    return answer
