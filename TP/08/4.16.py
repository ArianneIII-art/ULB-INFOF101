def joindre(jointure: str, mots: list[str])->str:
	res = mots[0]
	for i in range(1, len(mots)):
		res += jointure + mots[i]
	return res

mots = ["Salut", "je programme", "en python"]
print(joindre("--", mots))
