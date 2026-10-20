def acrostiche(file_name):
    res = ""
    with open(file_name, "rt") as f:
        for line in f:
            res += line[0]
    return res