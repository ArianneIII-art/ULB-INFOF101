from random import randint

def deviner_nombre(nombre: int | None = None):
    if nombre is None:
        nombre = randint(1,100)

    user_input = int(input(">>> "))

    while user_input != nombre:
    	if user_input < nombre:
    		print("trop petit")
    	else:
    		print("trop grand")

    	user_input = int(input(">>> "))

    print(f"trouve, le nbr étais {nombre}")