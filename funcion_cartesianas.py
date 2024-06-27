import math as m

fichero1 = open("tabla_polares.dat", "r")
fichero2 = open("tabla_cartesianas.dat", "w")

lista1 = fichero1.readlines()
fichero2.write("Tabla de coordenadas (x,y) para trayectoria parabolica:\n    x [UA] \t\t\t    y [UA]\n")

for i in range(2, len(lista1)):
    fila = lista1[i].split()
    x = -1 * float(fila[1]) * m.cos(float(fila[0]))
    y =      float(fila[1]) * m.sin(float(fila[0]))

    fichero2.write("{}   \t {}\n".format(x, y))

fichero1.close()
fichero2.close()