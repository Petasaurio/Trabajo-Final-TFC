import math as m

def polares(RP, num):         #toma el perihelio y un numero para ordenar los multiples archivos de coordenadas
    fichero = open("datos/polar/tablaPolares_{}.dat".format(num), "w")
    fichero.write("Tabla del radio en funcion del angulo para trayectoria parabolica de perihelio {} UA:\n   Angulo [rad]\t\t\t\t Radio [UA]\n".format(RP))

    theta = -3/4*m.pi                                     #valor inicial de theta

    while theta <= 3/4*m.pi:                              #iteraciones con sentencia while para calcular los radios y escribirlos en el fichero en funcion de los ángulos
        r = 2*RP/(1+m.cos(theta))
        fichero.write("{}\t\t\t{}\n".format(theta, r))
        theta += 0.005

    fichero.close()

def cartesianas(num):
    ficheroPol = open("datos/polar/tablaPolares_{}.dat".format(num), "r")                   #abrir ficheros para leer y escribir
    ficheroCar = open("datos/cartesiana/tablaCartesianas_{}.dat".format(num), "w")

    listaPol = ficheroPol.readlines()
    ficheroCar.write("Tabla de coordenadas (x,y) para trayectoria parabolica:\n\t x [UA] \t\t\t\t y [UA]\n")

    for i in range(2, len(listaPol)):                     #iteraciones con sentencia for para convertir los datos polares en cartesianos y escribirlos
        fila = listaPol[i].split()
        x = -1 * float(fila[1]) * m.cos(float(fila[0]))
        y =      float(fila[1]) * m.sin(float(fila[0]))

        ficheroCar.write("{}   \t {}\n".format(x, y))

    ficheroPol.close()
    ficheroCar.close()