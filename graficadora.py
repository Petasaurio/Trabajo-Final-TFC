import matplotlib.pyplot as plt
import math as m
import coordenadas as c

def graficaParte1(opcion):  # valores de opcion: 
                            #   1 -> grafica opcional de las distintas trayectorias posibles
                            #   0 -> grafica estandar de la trayectoria observada
    # Se genera y dibuja la trayectoria de la Tierra primero

    lista_xtierra=[]
    lista_ytierra=[]
    theta=0

    while theta <= 2*m.pi:  #iteraciones con sentencia while para crear listas con las coordenadas de la orbita terrestre
        lista_xtierra.append( m.cos(theta) )
        lista_ytierra.append( m.sin(theta) )
        theta += 0.005

    plt.plot(lista_xtierra, lista_ytierra, color="red", linestyle="dashed", label="Orbita de la tierra")
    plt.scatter([0], [0], marker="o", s=100, color="#FFC714")  

    # Luego se genera la/s trayectoria/s del cometa en función de la opcion seleccionada

    lista_RP=[0.22674, 0.1, 0.25, 0.5, 0.75, 1] # se trabaja con la lista de posibles valores

    if opcion:
        extremo = 6 # en caso de seleccionarse la opcion, en el [for n] el rango recorre toda la lista_RP
        paletaColores = ["#e08295", "#e0d382", "#82c7e0", "#e0a382", "#8fe082"] # Paleta generada para dar color a las curva de la linea 49
    else:
        extremo = 1 # en caso contrario se usa solo el primer elemento

    for n in range (0, extremo):
        c.polares(lista_RP[n], n)
        c.cartesianas(n)
        fichero = open("datos/cartesiana/tablaCartesianas_{}.dat".format(n), "r")        #abrir archivo de datos para su lectura
        lista = fichero.readlines()
        lista_x = []
        lista_y = []

        for i in range(2, len(lista)):  #iteraciones con sentencia for para guardar la informacion del archivo en lista_x y lista_y
            fila = lista[i].split()
            lista_x.append( float(fila[0]) )
            lista_y.append( float(fila[1]) )
        fichero.close()

        if not n:
            plt.plot(lista_x, lista_y, label="Trayectoria del cometa C/1823 Y1")  
        else:
            plt.plot(lista_x, lista_y, linestyle ="dashed", color=paletaColores[n-1], label="Trayectoria del cometa C/1823 Y1 con RP = {}".format(lista_RP[n]))

    #Configuracion de detalles para pulir la grafica
    plt.grid()                      
    plt.xlabel( "x [UA]" )
    plt.ylabel( "y [UA]" )
    plt.legend(loc="upper left")
    plt.axis("equal")
    
    if opcion:
        plt.title("Trayectoria de cometas con distinto Radio del Perihelio y la orbita de la Tierra")
        plt.savefig("graficas/graficaOpcional.pdf", dpi=500)
    else:
        plt.title("Trayectoria del cometa C/1823 Y1 y la orbita de la Tierra")
        plt.savefig("graficas/grafica.pdf", dpi=500)
    
    plt.show()