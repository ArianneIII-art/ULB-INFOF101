def file_histogram(fileName):
    with open(fileName) as f:
        txt = f.read()
        dico = dict()
        for i in txt:
            if i not in dico:
                dico[i] = 1
            else:
                dico[i] += 1
    
    return dico

def words_by_length(fileName):
    with open(fileName) as f:
        current_word = ""
        dico = dict()
        txt = f.read()
        for i in txt:
            i = i.lower()
            if i.isalpha():
                current_word += i
            else:
                if current_word:
                    if len(current_word) not in dico:
                        dico[len(current_word)] = list()
                        dico[len(current_word)].append(current_word)
                    else:
                        if current_word not in dico[len(current_word)]:
                            dico[len(current_word)].append(current_word)
                    current_word = ""
        
        for i in dico:
            dico[i].sort()

        return dico

print(words_by_length("./Zola.txt"))