def dupliques (a):
    for i in range(len(a)):
        for c in range(i+1, len(a)):
            if a[i] == a[c]:
                return True
    
    return False