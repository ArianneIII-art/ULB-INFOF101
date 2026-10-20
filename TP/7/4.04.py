def indice_maximum(elements: list)-> int:
    return len(elements) -1

def trouver_maximum(elements: list):
    elements.sort()
    return elements[-1]