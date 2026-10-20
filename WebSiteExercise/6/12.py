def belongs_to_file(word, filename):
    with open(filename) as f:
        return word in f.read()