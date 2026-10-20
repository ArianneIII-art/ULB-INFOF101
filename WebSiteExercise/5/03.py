def duree(debut, fin):
    if debut[0] < fin[0]:
        if (fin[1] - debut[1]) >= 0:
            return (fin[0]-debut[0], fin[1]-debut[1])
        else:
            return (fin[0]-debut[0]-1, fin[1]-debut[1]+60)
    else:
        if debut[1] - fin[1] >= 0:
            return (duree((0,0), (24-(debut[0]-fin[0]), fin[1]-debut[1])))
        else:
            to_return = duree((0,0), (24-(debut[0]-fin[0]), (fin[1]-debut[1]))) 
            return (to_return)