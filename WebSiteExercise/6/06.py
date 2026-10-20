def symetrise_amis(d: dict, add_or_cut: bool) -> None:
    if add_or_cut:
        for i in d:
            for j in d[i]:
                if i not in d[j]:
                    d[j].add(i)
    else:
        for i in d:
            for j in d[i]:
                if i not in d[j]:
                    temp = set()
                    for c in d[i]:
                        if c != j:
                            temp.add(c)
                        d[i] = temp