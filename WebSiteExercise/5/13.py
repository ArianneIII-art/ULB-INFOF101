def my_insert(l, n):
    assert isinstance(n, int)

    if len(l) == 0:
        l.append(n)
    else:
        i = len(l)-1

        while (l[i] >= n) and (i >= 0):
            i -= 1
        i += 1

        if len(l)-i != 0:
            l = l.insert(i, n)
        else:
            l =  l.append(n)