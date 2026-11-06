def deux_egaux(a, b, c):
	if a == b or a == c or b == c:
		return True
	return False

print(deux_egaux(1,2,3))
print(deux_egaux(1,1,2))
print(deux_egaux(1,2,2))
print(deux_egaux(3,2,3))
print(deux_egaux(1,3,3))
