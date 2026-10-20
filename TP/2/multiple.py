a, b = int(input()), int(input())

if a < 0 or b < 0:
	print("Error : one of the two parameter was negative")
	exit()
elif a % b != 0 and b % a != 0:
	print("a et b ne sont pas multiples l’un de l’autre")
