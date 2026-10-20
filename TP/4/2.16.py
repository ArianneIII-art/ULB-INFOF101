x = input()
voyelle = 0

for i in x:
    if i.lower() in ["a","e","i","o","u","y","é", "è", "à", "ù"]:
        voyelle += 1

print(voyelle)