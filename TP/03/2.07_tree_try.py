PASSWORD="value"
x = input('>>> ')
i = 1

while x != PASSWORD and i < 3:
	x = input("Password Incorrect, try again \n>>> ")
	i += 1

if x != PASSWORD:
	print("Three attempt incorrect")
else:
	print("Password correct")
