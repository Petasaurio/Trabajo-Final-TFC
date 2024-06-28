#este script lee el archivo creado por funcion_polares.py para convertir las coordenadas polares a cartesianas y guardarlas en un nuevo archivo
import math as m

fichero1 = open("tabla_polares5.dat", "r")                   #abrir ficheros para leer y escribir
fichero2 = open("tabla_cartesianas5.dat", "w")

lista1 = fichero1.readlines()
fichero2.write("Tabla de coordenadas (x,y) para trayectoria parabolica:\n\t x [UA] \t\t\t\t y [UA]\n")

for i in range(2, len(lista1)):                     #iteraciones con sentencia for para convertir los datos polares en cartesianos y escribirlos
    fila = lista1[i].split()
    x = -1 * float(fila[1]) * m.cos(float(fila[0]))
    y =      float(fila[1]) * m.sin(float(fila[0]))

    fichero2.write("{}   \t {}\n".format(x, y))

fichero1.close()
fichero2.close()