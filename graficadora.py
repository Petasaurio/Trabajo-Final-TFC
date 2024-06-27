import matplotlib.pyplot as plt
import math as m

fichero = open("tabla_cartesianas.dat", "r")

lista = fichero.readlines()

lista_x = []
lista_y = []

for i in range(2, len(lista)):
    fila = lista[i].split()

    lista_x.append( float(fila[0]) )
    lista_y.append( float(fila[1]) )

fichero.close()

lista_xtierra=[]
lista_ytierra=[]
theta=0

while theta <= 2*m.pi:
    lista_xtierra.append( m.cos(theta) )
    lista_ytierra.append( m.sin(theta) )
    theta += 0.005

plt.plot(lista_x, lista_y, label="Trayectoria del cometa C/1823 Y1")
plt.scatter([0], [0], marker="o", color="yellow")
plt.plot(lista_xtierra, lista_ytierra, color="red", linestyle="dashed", label="Orbita de la tierra")

plt.grid()
plt.title("Trayectoria del cometa C/1823 Y1 y la orbita de la Tierra")
plt.xlabel( "x [UA]" )
plt.ylabel( "y [UA]" )
plt.legend(loc="upper left")
plt.axis("equal")
plt.show()