def my_insert(l, n):
    if type(n) != int:
        return None
    if len(l) == 0:
        return [n]

    i = len(l)-1

    while (l[i] >= n) and (i >= 0):
        i -= 1
    i += 1

    if len(l)-i != 0:
        l = l[:i] + [n] + l[-(len(l)-i):]
    else:
        l =  l[:i] + [n]
    return l