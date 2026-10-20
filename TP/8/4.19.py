def to_int(texte: str)-> int | None:
        if not(texte.isdigit()):
                return None

        res = 0
        for i in range(len(texte)-1, -1, -1):
                res += (ord(texte[i]) - ord('0')) * 10**(len(texte)-i-1)

        return res

def to_float(texte: str)-> float | None:
	texte = texte.split('.')

	if len(texte) > 2 or not(texte[0]):
		return None

	texte[0] = to_int(texte[0])

	if len(texte) == 2:
		i = len(texte[1])
		texte[1] = to_int(texte[1])
		return texte[0] + texte[1] * 10**-(i)
	else:
		return texte[0] /1


print(to_float(""))
print(to_float("12"))
print(to_float("1.2"))
print(to_float("11.12"))
print(to_float("123456"))
print(to_float("0.987"))
print(to_float("1.1.1.1"))
