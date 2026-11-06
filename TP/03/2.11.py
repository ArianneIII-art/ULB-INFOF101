nbr = int(input(" >>> "))

if nbr < 1:
	print("erreur, le nombre doit etre strictement positif")
	exit()

print(nbr)
while nbr != 1:
	if nbr % 2 == 0:
		nbr /= 2
	else:
		nbr = 3*nbr+1

	print(int(nbr))
