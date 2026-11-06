def trouver_meilleur_cv(candidatures: list[tuple])-> str:
    winner = ["", -1]
    for i in candidatures:
        current = [i[0], 0]
        for j in i[1]:
            if j in COMPETENCES_SOUHAITEES:
                current[1] += 1
        if current[1] > winner[1]:
            winner = current
    return winner[0]







COMPETENCES_SOUHAITEES = {"Python", "Assembleur", "Travail d’équipe", "Gestion de projet", "JavaScript"}
candidatures = [
                    ("Alice", {"Python", "Travail d’équipe", "Machine Learning"}),
                    ("Bob", {"Python", "JavaScript", "Gestion de projet", "SQL"}),
                    ("Charlie", {"Assembleur", "Travail d’équipe", "JavaScript"}),
                    ("David", {"Python", "Assembleur", "Gestion de projet"}),
                    ("Eve", {"Travail d’équipe", "JavaScript"})
               ]

print(trouver_meilleur_cv(candidatures))
