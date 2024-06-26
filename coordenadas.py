# Funcion para crear tablas de datos en polares. Toma el perihelio, un numero que usa para ordenar los multiples archivos que crea y el angulo que define el intervalo de trabajo

def polares(RP, num, ang_max):
    import math as m

    fichero = open("datos/polar/tablaPolares_{}.dat".format(num), "w")
    fichero.write("Tabla del radio en funcion del angulo para trayectoria parabolica de perihelio {} UA:\n   Angulo [rad]\t\t\t\t Radio [UA]\n".format(RP))

    theta = -ang_max                            # valor inicial de theta, arranca desde el valor opuesto al maximo y terminará en el maximo

    while theta <= ang_max:                     # iteraciones con sentencia while para calcular los radios y escribirlos en el fichero en funcion de los ángulos
        r = 2*RP/(1+m.cos(theta))
        fichero.write("{}\t\t\t{}\n".format(theta, r))
        theta += 0.005

    fichero.close()


# Funcion para crear tablas de datos en cartesianas. 'num' sirve para buscar el archivo de coordenadas polares que corresponda

def cartesianas(num):
    import math as m

    ficheroPol = open("datos/polar/tablaPolares_{}.dat".format(num), "r")                   # abrir ficheros para leer y escribir
    ficheroCar = open("datos/cartesiana/tablaCartesianas_{}.dat".format(num), "w")

    listaPol = ficheroPol.readlines()                                                       # separar tabla en lista de strings y escribir titulo de nueva tabla
    ficheroCar.write("Tabla de coordenadas (x,y) para trayectoria parabolica:\n\t x [UA] \t\t\t\t y [UA]\n")

    for i in range(2, len(listaPol)):           # iteraciones con sentencia for para convertir los datos polares en cartesianos y escribirlos
        fila = listaPol[i].split()
        x = -1 * float(fila[1]) * m.cos(float(fila[0]))
        y =      float(fila[1]) * m.sin(float(fila[0]))

        ficheroCar.write("{}   \t {}\n".format(x, y))

    ficheroPol.close()
    ficheroCar.close()


# Funcion que dado un angulo theta, devuelve el instante de tiempo (en segundos) en el que pasa por alli

def kepler(theta):
    import math as m

    RP=0.22674*1.496E11                  # conversion de RP de UA a metros
    G=6.67E-11                           # constante de gravitacion universal en [N m^2 kg^-2]
    M=1.989E30                           # masa del sol en [kg]

    VP= m.sqrt(2*G*M/RP)                 # velocidad en el perihelio en m/s
    K=(G**2)*(M**2)/(RP**3)/(VP**3)      # constante K en s^-1

    t = ( m.tan(theta/2)**3 + 3*m.tan(theta/2) ) / (6*K)         # calculo del tiempo con la ecuacion de kepler  
    return t


# Funcion que dado un paso (salto de tiempo) y una cantidad de puntos, calcula las coordenadas en los tiempos correspondientes

def intervalosT(paso, cant_puntos):
    import math as m
    from metodo_biseccion import biseccion

    fichero = open("datos/kepler/tablaPuntosExtra.dat","w")      # abrir y escribir titulo de tabla a utilizar
    fichero.write("Tabla de coordenadas x e y en funcion del tiempo con saltos de {} segundos\n".format(paso))
    fichero.write("\t\t x [UA] \t\t\t y [UA] \t\t\t Tiempo [s]\n")

    for i in range(1,cant_puntos+1):                 # iteraciones para calcular coordenadas a partir de la funcion 'biseccion' y escribir el fichero
        theta = biseccion(i*paso, 0.001)             # se elije arbitrariamente un error igual a 0.001
        r = 2 * 0.22674 / (1+m.cos(theta[0]))
        x_temp = (-1)*r*m.cos(theta[0]) 
        y_temp =      r*m.sin(theta[0])
            
        fichero.write("{} \t {} \t {} \n".format(x_temp, y_temp, i*paso))
    
    fichero.close()