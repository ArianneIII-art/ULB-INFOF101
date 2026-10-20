def my_filter(lst, f):
    res = []
    for i in lst:
        if f(i):
            res.append(i)
    return res