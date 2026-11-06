x, tot = int(input()), 0

if x <= 0:
	print("This program require a positive number")
	exit()

i=0
while i <= x:
	tot += i
	i+=1

print(tot)
