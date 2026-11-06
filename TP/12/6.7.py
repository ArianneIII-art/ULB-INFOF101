def recensement(etudiants: list)-> tuple:
    name, sex = {},{}
    for i in etudiants:
        name[i["prenom"]] = name.get(i["prenom"], 0) + 1
        sex[i["genre"]] = sex.get(i["genre"], 0) + 1
    return name, sex



ETUDIANTS = [
    {"prenom": "Laura", "genre": "F", "classe": "1A"},
    {"prenom": "Ali", "genre": "M", "classe": "1A"},
    {"prenom": "Achille", "genre": "X", "classe": "1A"},
    {"prenom": "Sourah", "genre": "F", "classe": "3B"},
    {"prenom": "Laura", "genre": "F", "classe": "3B"},
]
print(recensement(ETUDIANTS))
