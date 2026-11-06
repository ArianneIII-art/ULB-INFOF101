def initialiser_plateau(size=3):
	return [[None for _ in range(size)] for _ in range(size)]

def afficher_plateau(plateau):
	for i in plateau:
		for j in i:
			print(f"{j}", end="\t")
		print()
	print()

def jouer(plateau, joueur, ligne: int, colonne: int) -> bool:
	if plateau[ligne][colonne] is None and ligne < len(plateau) and colonne < len(plateau[0]):
		plateau[ligne][colonne] = joueur
		return True
	return False

def a_gagne(plateau, joueur, size=3) -> bool:
	win = [joueur for _ in range(size)]
	# LIGNE
	for i in range(size):
		if plateau[i] == win:
			return True

	# COLLONNE
	for i in range(size):
		if [plateau[j][i] for j in range (size)] == win:
			return True

	# DIAGONALE
	if [plateau[i][i] for i in range (size)] == win or [plateau[i][-(i+1)] for i in range (size)] == win:
		return True


test = initialiser_plateau()
afficher_plateau(test)
jouer(test, 'X', 0,0)
afficher_plateau(test)
jouer(test, 'O', 0,0)
afficher_plateau(test)
jouer(test, 'X', 1,1)
jouer(test, 'X', 2,2)
afficher_plateau(test)
print(a_gagne(test, "X"))
