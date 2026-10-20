def to_int(texte: str)-> int | None:
	if not(texte.isdigit()):
		return None

	res = 0
	for i in range(len(texte)-1, -1, -1):
		res += (ord(texte[i]) - ord('0')) * 10**(len(texte)-i-1)

	return res

print(to_int("1234567890"))
