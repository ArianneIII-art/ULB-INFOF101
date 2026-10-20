def distance_points(pt1, pt2):
    return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5

def longueur(*points):
    somme = 0
    for i in range(1, len(points)):
        somme += distance_points(points[i-1], points[i])
    return somme