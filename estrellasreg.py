import turtle

turtle.showturtle()

puntas= int(input("Seleccione el numero de puntas: "))
longitud = 100
angulo1 = (360/puntas) + 120
angulo2 = 180 - (360/puntas)
n = 1

if puntas != 0:
    angulo = angulo2
else:
    angulo = angulo1


turtle.fillcolor("red")

turtle.begin_fill()

for i in range(80):
    turtle.forward(longitud)
    turtle.right(angulo)

turtle.end_fill()