import matplotlib.pyplot as plt
import math as m
import coordenadas as c
from random import randrange

def randColor():
    paleta = ['#6832cf', '#1fdfdc', '#8815bd', '#b007cd', '#dea215', '#661a0e', '#6cb379', '#25917f', '#49698b', '#bf1d1c', '#490660', '#f4665a', '#6e7579', '#ece805', '#e5f5a7', '#cc99a6', '#17e341', '#ab0160', '#3afdfb', '#18ccb2', '#2a80bb', '#fb672b', '#903688', '#b9eae1', '#ea558b', '#402273', '#adc67f', '#fccc65', '#7aeb38', '#699589', '#efaed1', '#173121', '#385967', '#cd9c86', '#b94094', '#716343', '#cf39ce', '#f5f273', '#706562', '#2061bd', '#bbe4c1', '#0ed219', '#acd54a', '#09a584', '#dcc687', '#2a2780', '#a50101', '#39eb1b', '#cec47e', '#cb3f22', '#98749f', '#5549cc', '#c6673f', '#539fab', '#838f83', '#f0a312', '#839673', '#5de4f9', '#40acae', '#860dab', '#8cb0a7', '#dc14e6', '#10a8f8', '#8c9d8e', '#05cdb1', '#1f67d5', '#89b4b5', '#abfd77', '#93f883', '#5cc3d5', '#0ff16c', '#db3b96', '#4a13c5', '#944c0b', '#0d20ba', '#43faf6', '#0795bc', '#e482f7', '#091c3e', '#b556b0', '#4b9dc5', '#25dd72', '#431735', '#ce8ba6', '#70ee63', '#cd8bb5', '#efafe9', '#af9f38', '#b99c3c', '#a46d1e', '#475ca1', '#2f97dd', '#b53e97', '#f4af17', '#756391', '#4f93b9', '#e05e83', '#ec3d78', '#e18096', '#d3e3ec']
    return paleta[randrange(0, len(paleta))] # Desvuelve un color aleatorio

def plotFichero(fichero, opcion, RP): # Valores de opcion consistentes con los de graficar(), RP necesario solo si opcion == 1
    lista=fichero.readlines()
    lista_x = []
    lista_y = []

    for i in range(2, len(lista)):          # iteraciones con sentencia for para guardar la informacion de los archivos en lista_x y lista_y
        fila = lista[i].split()
        lista_x.append( float(fila[0]) )
        lista_y.append( float(fila[1]) )
    fichero.close()    

    if opcion == 0:                         # segun la iteracion que sea, graficar las distintas trayectorias con sus propiedades
        plt.plot(lista_x, lista_y, label="Trayectoria del cometa C/1823 Y1") 
    elif opcion == 1:
        plt.plot(lista_x, lista_y, linestyle ="dashed", color=randColor(), label="Trayectoria del cometa C/1823 Y1 con RP = {}".format(RP))
    elif opcion == 2:
        plt.scatter(lista_x, lista_y, label="Posiciones a 1, 2 y 3 meses del perihelio", s=25, marker="x",color=randColor())
    elif opcion == 3:
        plt.scatter(lista_x, lista_y, label="Posicion cada 77760 segundos (21.6 horas) despues del perihelio", s=25, marker="+", color=randColor())

def graficar(opcion):  # valores de opcion:
                       #   0 -> grafica estandar de la trayectoria observada
                       #   1 -> grafica opcional de las distintas trayectorias posibles
                       #   2 -> grafica con coordenadas a 1, 2 y 3 meses
                       #   3 -> grafica de intervalos de tiempo de 0 a 3 meses
    

# Se genera y dibuja la trayectoria de la Tierra primero
   
    lista_xtierra=[]
    lista_ytierra=[]
    theta=0

    while theta <= 2*m.pi:               # iteraciones con sentencia while para crear listas con las coordenadas de la orbita terrestre
        lista_xtierra.append( m.cos(theta) )
        lista_ytierra.append( m.sin(theta) )
        theta += 0.005

    plt.plot(lista_xtierra, lista_ytierra, color="red", linestyle="dashed", label="Orbita de la tierra")
    plt.scatter([0], [0], label="Sol", marker="o", s=100, color="#FFC714")  


# Segun cada caso, se realizan distintos calculos necesarios previos a ir a graficar la/s trayectoria/s 

    if opcion == 0 or opcion == 1:
        ang_max = 3/4*m.pi
    else:
        ang_max = 4/5*m.pi

# Se grafica la trayectoria del cometa

    c.polares(0.22674, 0, ang_max)
    c.cartesianas(0)
    plotFichero(open("datos/cartesiana/tablaCartesianas_0.dat", "r"), 0, None) # Se dibuja la trayectoria del cometa

# evaluar el procedimiento a realizar en función de la opcion

    if opcion == 1:
        for n in range (0, 5):
            lista_RP=[0.1, 0.25, 0.5, 0.75, 1]   # se trabaja con la lista de posibles valores de RP
            c.polares(lista_RP[n], n+1, ang_max)
            c.cartesianas(n+1)
            plotFichero(open("datos/cartesiana/tablaCartesianas_{}.dat".format(n), "r"), opcion, lista_RP[n])            
    elif opcion == 2:                  # segun que iteracion que sea, se llama a distintas funciones para crear las tablas de datos correspondientes
        c.intervalosT(2592000, 3)
        plotFichero(open("datos/kepler/tablaPuntosExtra.dat", "r"), opcion, None)       
    elif opcion == 3:
        c.intervalosT(77760, 100)
        plotFichero(open("datos/kepler/tablaPuntosExtra.dat", "r"), opcion, None)
            

# Configuracion de detalles para pulir la grafica
    
    plt.grid()                      
    plt.xlabel( "x [UA]" )
    plt.ylabel( "y [UA]" )
    plt.legend(loc="upper left")
    plt.axis("equal")
    
    if opcion == 0:          # titulos y guardado de archivos
        plt.title("Trayectoria del cometa C/1823 Y1 y la orbita de la Tierra")
        plt.savefig("graficas/grafica_1.pdf", dpi=500)
    elif opcion == 1:
        plt.title("Trayectoria de cometas con distinto Radio del Perihelio y la orbita de la Tierra")
        plt.savefig("graficas/graficaOpcional_1.pdf", dpi=500)
    elif opcion == 2:
        plt.title("Trayectoria del cometa C/1823 Y1 y posiciones a 1, 2 y 3 meses del perihelio")
        plt.savefig("graficas/grafica_2.pdf", dpi=500)
    elif opcion == 3:
        plt.title("Trayectoria del cometa C/1823 Y1 y posiciones adicionales luego del perihelio")
        plt.savefig("graficas/graficaOpcional_2.pdf", dpi=500)
    
    plt.show()