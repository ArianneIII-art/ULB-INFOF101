def compter_chiffres(x: int)-> int:
	i = 0
	if x < 0:
		x = -x
	while x != 0:
		x //= 10
		i += 1
	return i

def est_armstrong(nbr: int)-> bool:
	x = nbr
	nbr_chiffre = compter_chiffres(nbr)
	tot = 0

	while x != 0:
		tot += (x % 10) ** nbr_chiffre
		x //= 10

	return tot == nbr

print(
est_armstrong(9),
est_armstrong(10),
est_armstrong(153),
sep="\n")
