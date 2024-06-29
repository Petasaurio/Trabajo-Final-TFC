import matplotlib.pyplot as plt
import math as m
import coordenadas as c
from metodo_biseccion import biseccion

def graficaParte1(opcion):  # valores de opcion:
                            #   1 -> grafica estandar de la trayectoria observada
                            #   2 -> grafica opcional de las distintas trayectorias posibles
                            #   3 -> grafica con coordenadas a 1, 2 y 3 meses
                            #   4 -> grafica de intervalos de tiempo de 0 a 3 meses
    

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
    paletaColores = ["#e08295", "#e0d382", "#82c7e0", "#e0a382", "#8fe082", "#e86f1e", "#6319d1"]     # Paleta generada para dar color a las distintas curvas

    if opcion == 1:
        extremo = 1          # para que el for de la seccion siguiente solo ejecute la primera iteracion, es decir la del cometa
        ang_max = 3/4*m.pi
    elif opcion == 2:
        extremo = 6             # en la opcion 1, en el [for n] el rango recorre toda la lista_RP
        ang_max = 3/4*m.pi
    elif opcion == 3:
        extremo = 7             # en la opcion 2, dejo extremo=1 para que más adelante se grafique la trayectoria del cometa normalmente
        ang_max = 4/5*m.pi      #pongo para que se grafique una curva más larga así el punto a 3 meses del perihelio no queda afuera
    else:
        extremo = 8
        ang_max = 4/5*m.pi
   


# crear listas y graficar trayectorias de el/los cometa/s

    for n in range (0, extremo):
        if (opcion==3 and n!=0 and n!=6) or (opcion==4 and n!=0 and n!=7):
            continue


        if n <= 5:
            c.polares(lista_RP[n], n, ang_max)
            c.cartesianas(n)
            fichero = open("datos/cartesiana/tablaCartesianas_{}.dat".format(n), "r")        # abrir archivo de datos para su lectura
        elif n == 6:
            c.intervalosT(2592000, 3)
            fichero = open("datos/parte2/tablaPuntosExtra.dat", "r")
        elif n == 7:
            c.intervalosT(77760, 100)
            fichero = open("datos/parte2/tablaPuntosExtra.dat", "r")
        

        lista=fichero.readlines()
        lista_x = []
        lista_y = []

        for i in range(2, len(lista)):          # iteraciones con sentencia for para guardar la informacion del archivo en lista_x y lista_y
            fila = lista[i].split()
            lista_x.append( float(fila[0]) )
            lista_y.append( float(fila[1]) )
        fichero.close()


        if n == 0:
            plt.plot(lista_x, lista_y, label="Trayectoria del cometa C/1823 Y1") 
        elif n>=1 and n<=5:
            plt.plot(lista_x, lista_y, linestyle ="dashed", color=paletaColores[n-1], label="Trayectoria del cometa C/1823 Y1 con RP = {}".format(lista_RP[n]))
        elif n == 6:
            plt.scatter(lista_x, lista_y, label="Posiciones a 1, 2 y 3 meses del perihelio", s=25, color=paletaColores[n-1])
        elif n == 7:
            plt.scatter(lista_x, lista_y, label="Posicion cada 77760 segundos (21.6 horas) despues del perihelio", s=25, color=paletaColores[n-1])


# Configuracion de detalles para pulir la grafica
    
    plt.grid()                      
    plt.xlabel( "x [UA]" )
    plt.ylabel( "y [UA]" )
    plt.legend(loc="upper left")
    plt.axis("equal")
    
    if opcion == 1:          # hay que corregir esto!!!!!!!!!
        plt.title("Trayectoria del cometa C/1823 Y1 y la orbita de la Tierra")
        plt.savefig("graficas/grafica1.pdf", dpi=500)
    elif opcion == 2:
        plt.title("Trayectoria de cometas con distinto Radio del Perihelio y la orbita de la Tierra")
        plt.savefig("graficas/grafica1_Opcional.pdf", dpi=500)
    elif opcion == 3:
        plt.title("Trayectoria del cometa C/1823 Y1 y posiciones a 1, 2 y 3 meses del perihelio")
        plt.savefig("graficas/grafica2.pdf", dpi=500)
    elif opcion == 4:
        plt.title("Trayectoria del cometa C/1823 Y1 y posiciones adicionales luego del perihelio")
        plt.savefig("graficas/grafica2_Opcional.pdf", dpi=500)
    
    plt.show()