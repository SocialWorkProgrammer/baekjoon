def solution(players, callings):
    playerdict = {player : i for i, player in enumerate(players)}
    for name in callings:
        front, back = playerdict[name]-1, playerdict[name]
        playerdict[players[front]] += 1
        playerdict[players[back]] -= 1
        players[front], players[back] = players[back], players[front]

    return players
