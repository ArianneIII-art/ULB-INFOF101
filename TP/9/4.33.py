def couper(nombres: list, marqueur: int) -> tuple[list]:
	for i in range(len(nombres)):
		if nombres[i] == marqueur:
			return nombres[:i], nombres[i+1:]
	return nombres, []

print(
couper([-5, 7, 4, 10], 4),
couper([-5, 7, 4, 10], 42),
sep="\n"
)
