# estrellas-regulares
El enlace de mi repositorio es: https://github.com/carmenm02/estrellas-regulares.git

El trabajo consiste en crear una estrella con la cantidad de puntas que queramos y para ello debemos de calcular los ángulos necesarios

El codigo que he usado es:

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

El diagrama de flujo es el siguiente:
<img width="787" alt="figma" src="https://user-images.githubusercontent.com/91721886/146836300-a0ca87e3-76ef-4dd7-9adc-9bf4c12d943d.png">
