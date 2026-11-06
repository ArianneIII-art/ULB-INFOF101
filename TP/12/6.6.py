def calculer_totaux(points: dict[str, tuple])-> dict[str, float]:
    res = dict()
    for i in points:
        res[i] = sum(points[i])
    return res

def trouver_gagnants(totaux: dict[str, float]) -> tuple[list[str], float]:
    best = -1.0
    winner = []
    for i in totaux:
        if totaux[i] > best:
            best = totaux[i]
            winner = [i]
        elif totaux[i] == best:
            winner.append(i)
    return winner, best


notes = {
    "Alexandre": (12, 0, 12),
    "Sélim": (0, 16.5, 13),
    "Luc": (0, 0, 0),
    "Marie": (14, 14.5, 0),
    "Georges": (19, 19, 0),
    "Inès": (19, 5, 14)
}
tot = calculer_totaux(notes)
print(tot)
print(trouver_gagnants(tot))

