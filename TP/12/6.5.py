def compter_occurrences(elements: list)-> dict:
    res = {}
    for i in elements:
        res[i] = res.get(i, 0) + 1
    return res

def afficher_histogramme(occurrences: dict):
    key = list(occurrences.keys())
    key.sort()
    for i in key:
        print(i, "*"*occurrences[i])

elements = [2, 3, 1, 4, 4, 5, 2, 2, 1, 2]

occurrences_par_element = compter_occurrences(elements)

afficher_histogramme(occurrences_par_element)
