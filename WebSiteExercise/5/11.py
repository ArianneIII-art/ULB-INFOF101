def intersection(v, w):
    longuest_intersection = ""
    # use a double for to watch it (escape with break or maube while)
    # take advantage of the [1:2] is equivalent to [1]
    for i in range(len(v)):
        for j in range(i, len(v)+1):
            if v[i:j] in w:
                if len(longuest_intersection) < len(v[i:j]):
                    longuest_intersection = v[i:j]
    
    return longuest_intersection