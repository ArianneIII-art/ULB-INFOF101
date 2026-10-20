nbr_list = []

for i in range (3):
    nbr_list.append(int(input()))

if nbr_list[0] == nbr_list[1] or nbr_list[0] == nbr_list[2]:
    print(nbr_list[0])

elif nbr_list[1] == nbr_list[2]:
    print(nbr_list[1])