from math import pi, cos, sin

user_input=float(input())

for i in range(6):
    print(cos(i*(pi/3))*user_input, sin(i*(pi/3))*user_input)