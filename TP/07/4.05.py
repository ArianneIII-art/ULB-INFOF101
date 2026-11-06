# euivalent a la fct built in enumerate
def enumerer(liste: list)-> list[tuple]:
    to_return = []
    for i in range(len(liste)):
        to_return.append((i, liste[i]))
    return to_return

liste = ["Salut", "comment", "ça", "va?"]
for i, element in enumerer(liste):
    print(i, element)


liste = ["Salut", "comment", "ça", "va?"]
for i, element in enumerate(liste):
    print(i, element)