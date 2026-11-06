def compter_chiffres(x: int)-> int:
	i = 0
	if x < 0:
		x = -x
	while x != 0:
		x //= 10
		i += 1
	return i

print(
compter_chiffres(1),
compter_chiffres(12),
compter_chiffres(123),
compter_chiffres(1234),
compter_chiffres(12345),
compter_chiffres(-2432),
sep="\n")
