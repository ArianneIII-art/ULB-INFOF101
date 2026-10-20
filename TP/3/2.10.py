pv = 100

while 0 < pv < 200:
	x = input(f"prenez soin de votre plante carnivore : {pv}\n>>> ")

	if x == "mouche":
		pv += 10
	elif x == "eau":
			pv += 1
	elif x == "steak":
		pv += 100
	else:
		pv -= 50

if pv < 1:
	print("votre plante carnivore est morte")
else:
	print("Votre plante carnivore vous a dévoré")
