def inverser(liste: list)-> None:
	for i in range(len(liste)//2):
		liste[i], liste[-(i+1)] = liste[-(i+1)], liste[i]

elements = [1, 2, 3, 4, 5]
inverser(elements)
print(elements)
