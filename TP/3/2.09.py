from random import randint

NOMBRE_SECRET = randint(1, 100)

x = int(input(">>> "))

while x != NOMBRE_SECRET:
	if x < NOMBRE_SECRET:
		print("trop petit")
	else:
		print("trop grand")

	x = int(input(">>> "))

print(f"trouve, le nbr étais {NOMBRE_SECRET}")
