distance=[10, 10]
minute=[45, 43.50]
vitesse=[]

for i in range(len(distance)):
    vitesse.append(distance[i]/minute[i]*60)

for i in range(len(vitesse)):
    print(vitesse[i])

for i in range(len(vitesse)):
    print(vitesse[i]/1.61)