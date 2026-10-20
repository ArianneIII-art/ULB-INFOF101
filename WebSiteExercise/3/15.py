saut, position_cible, pos, trouve = int(input()), int(input()), 0, False
 
pos += saut
if pos != position_cible:
    print(pos)
else:
    trouve=True
 
while pos != 0 and trouve is False:
    pos += saut
    if pos >= 100:
        pos -= 100
    if pos != position_cible:
        print(pos)
    else:
        trouve=True
 
print("Cible atteinte" if trouve else "Pas trouvée")