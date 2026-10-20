def decompresse(l):
    to_return = []
    for i in l:
        for c in range(i[0]):
            to_return.append(i[1])
    return to_return