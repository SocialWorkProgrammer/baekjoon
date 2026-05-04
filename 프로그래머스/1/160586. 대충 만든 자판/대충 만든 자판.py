def solution(keymap, targets):
    keydict = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in keydict or keydict[key] > i + 1:
                keydict[key] = i + 1
    cnt = 0
    answer = []
    for target in targets:
        for tar in target:
            if tar not in keydict:
                cnt = -1
                break
            cnt += keydict[tar]
        answer.append(cnt)
        cnt = 0
    return answer
