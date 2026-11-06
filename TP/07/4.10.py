def distincts(elements: list)-> list:
	to_return = []
	for i in elements:
		if i not in to_return:
			to_return.append(i)
	return to_return

print(
	distincts([1, 2, 2, 3, 1]),
	distincts(['a', 'b', 'a']),
	sep="\n",
)
