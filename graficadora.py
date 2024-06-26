import matplotlib.pyplot as plt

fichero = open("tabla_cartesianas.dat", "r")

lista = fichero.readlines()

lista_x = []
lista_y = []

for i in range(1, len(lista)):
    fila = lista[i].split()

    lista_x.append( float(fila[0]) )
    lista_y.append( float(fila[1]) )

fichero.close()

plt.plot(lista_x, lista_y)
plt.axis("equal")
plt.show()