import matplotlib.pyplot as plt
import math as m
import coordenadas as c
from metodo_biseccion import biseccion

def graficaParte1(opcion):  # valores de opcion:
                            #   0 -> grafica estandar de la trayectoria observada
                            #   1 -> grafica opcional de las distintas trayectorias posibles
                            #   2 -> grafica con coordenadas a 1, 2 y 3 meses
    

# Se genera y dibuja la trayectoria de la Tierra primero
   
    lista_xtierra=[]
    lista_ytierra=[]
    theta=0

    while theta <= 2*m.pi:  #iteraciones con sentencia while para crear listas con las coordenadas de la orbita terrestre
        lista_xtierra.append( m.cos(theta) )
        lista_ytierra.append( m.sin(theta) )
        theta += 0.005

    plt.plot(lista_xtierra, lista_ytierra, color="red", linestyle="dashed", label="Orbita de la tierra")
    plt.scatter([0], [0], label="Sol", marker="o", s=100, color="#FFC714")  


# Segun cada caso, se realizan distintos calculos necesarios previos a ir a graficar la/s trayectoria/s 

    lista_RP=[0.22674, 0.1, 0.25, 0.5, 0.75, 1]             # se trabaja con la lista de posibles valores de RP
    paletaColores = ["#e08295", "#e0d382", "#82c7e0", "#e0a382", "#8fe082"]     # Paleta generada para dar color a las distintas curvas cuando se necesite

    if opcion == 0:
        extremo = 1          # para que el for de la seccion siguiente solo ejecute la primera iteracion, es decir la del cometa
        ang_max = 3/4*m.pi
    elif opcion == 1:
        extremo = 6             # en la opcion 1, en el [for n] el rango recorre toda la lista_RP
        ang_max = 3/4*m.pi
    elif opcion == 2:
        extremo = 1             # en la opcion 2, dejo extremo=1 para que más adelante se grafique la trayectoria del cometa normalmente
        ang_max = 4/5*m.pi      #pongo para que se grafique una curva más larga así el punto a 3 meses del perihelio no queda afuera

        fichero = open("datos/parte2/tablaPuntosExtra.dat","w")
        fichero.write("Tabla de coordenadas x e y para 1, 2 y 3 meses despues del perihelio\n")

        for i in range(1,4):                    # iteraciones para calcular coordenadas con 'biseccion', completar listas y escribir el fichero
            theta=biseccion(i*2592000, 0.001)             # se toma como que un mes tiene 30 dias = 2592000 segundos
            r = 2 * 0.22674 / (1+m.cos(theta[0]))
            x_temp = (-1)*r*m.cos(theta[0]) 
            y_temp =      r*m.sin(theta[0])
            
            fichero.write("{} mes \t {} \t {}\n".format(i,x_temp,y_temp))
            plt.scatter(x_temp, y_temp, label="Posicion a {} mes del perihelio".format(i), s=25, color=paletaColores[i])


# crear listas y graficar trayectorias de el/los cometa/s

    for n in range (0, extremo):
        c.polares(lista_RP[n], n, ang_max)
        c.cartesianas(n)
        fichero = open("datos/cartesiana/tablaCartesianas_{}.dat".format(n), "r")        # abrir archivo de datos para su lectura
        lista = fichero.readlines()
        lista_x = []
        lista_y = []

        for i in range(2, len(lista)):  # iteraciones con sentencia for para guardar la informacion del archivo en lista_x y lista_y
            fila = lista[i].split()
            lista_x.append( float(fila[0]) )
            lista_y.append( float(fila[1]) )
        fichero.close()

        if not n:
            plt.plot(lista_x, lista_y, label="Trayectoria del cometa C/1823 Y1")  
        else:
            plt.plot(lista_x, lista_y, linestyle ="dashed", color=paletaColores[n-1], label="Trayectoria del cometa C/1823 Y1 con RP = {}".format(lista_RP[n]))


# Configuracion de detalles para pulir la grafica
    
    plt.grid()                      
    plt.xlabel( "x [UA]" )
    plt.ylabel( "y [UA]" )
    plt.legend(loc="upper left")
    plt.axis("equal")
    
    if opcion == 0:          # hay que corregir esto!!!!!!!!!
        plt.title("Trayectoria del cometa C/1823 Y1 y la orbita de la Tierra")
        plt.savefig("graficas/graficaOriginal.pdf", dpi=500)
    elif opcion == 1:
        plt.title("Trayectoria de cometas con distinto Radio del Perihelio y la orbita de la Tierra")
        plt.savefig("graficas/graficaOpcional_1.pdf", dpi=500)
    elif opcion == 2:
        plt.title("Trayectoria del cometa C/1823 Y1 y posiciones adicionales")
        plt.savefig("graficas/graficaParte2.pdf", dpi=500)
    
    plt.show()