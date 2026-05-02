def solution(wallpaper):
    from math import inf
    files = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                files.append([i,j])
    mincoord = [inf, inf]
    maxcoord = [0,0]
    for file in files:
        if file[0] < mincoord[0]:
            mincoord[0] = file[0]
        if file[1] < mincoord[1]:
            mincoord[1] = file[1]
        if file[0] > maxcoord[0]:
            maxcoord[0] = file[0]
        if file[1] > maxcoord[1]:
            maxcoord[1] = file[1]
    maxcoord[0] += 1
    maxcoord[1] += 1
    answer = [*mincoord, *maxcoord]
    return answer
