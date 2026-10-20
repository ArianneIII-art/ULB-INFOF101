def nouveaux_heros(file, new_file):
    with open(file) as f:
        with  open(new_file, mode="w") as new_f:
            for i in f:
                i = i.replace("Pierre", "dummy")
                i = i.replace("Paul", "Tom")
                i = i.replace("Jacqueline", "Mathilde")
                i = i.replace("dummy", "Paul")
                new_f.write(i)