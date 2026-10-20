def insertion_sort(tab):
    tab = list(tab)
    for i in range (1, len(tab)):
        c = i-1
        temp = tab[i]
        tab.pop(i)
        while (c >= 0) and (temp < tab[c]):          
            c -= 1                                  
        tab.insert(c+1, temp)                        
    return ''.join(tab)                                      

def anagrammes(v, w):
    return insertion_sort(v) == insertion_sort(w)