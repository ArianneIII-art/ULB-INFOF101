# there is way more cleaner way to do that but i'm too lazy for them

def rotation(liste: list, n: int)-> list:
    res = []
    for index, element in enumerate(liste):
        if index + n < len(liste):
            res.append(liste[index+n])
        else:
            res.append(liste[index+n-len(liste)])
    return res

print(rotation([0, 1, 2, 3, 4, 5], 1),
[1, 2, 3, 4, 5, 0],
rotation([0, 1, 2, 3, 4, 5], 3),
[3, 4, 5, 0, 1, 2],
sep="\n")
