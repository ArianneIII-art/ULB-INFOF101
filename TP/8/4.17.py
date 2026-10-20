def est_adn(chaine: str) -> bool:
	if not(chaine):
		return False

	for i in chaine:
		if i not in ('A','T','C','G'):
			return False
	return True
