#con funcion_polares.py y funcion_cartesianas.py se crearon las 10 tablas de esta carpeta, aqui seran graficadas juntas
#el programa es similar a graficadora.py pero iterando 5 veces para incluir las 5 trayectorias parabolicas
import matplotlib.pyplot as plt

lista_RP=[0.1, 0.25, 0.5, 0.75, 1]                                    #lista de los RP con los que se calcularon las 5 trayectorias 

for j in range(5):
    fichero = open("tabla_cartesianas{}.dat".format(j+1), "r")        #abrir archivo de datos para su lectura

    lista = fichero.readlines()

    lista_x = []
    lista_y = []

    for i in range(2, len(lista)):              #iteraciones con sentencia for para guardar la informacion del archivo en lista_x y lista_y
        fila = lista[i].split()

        lista_x.append( float(fila[0]) )
        lista_y.append( float(fila[1]) )

    fichero.close()

    plt.plot(lista_x, lista_y, label="Trayectoria del cometa con RP={}".format(lista_RP[j]))

plt.grid()                              #configuracion de detalles para pulir la grafica
plt.title("Trayectoria de cometas con distinto Radio del Perihelio")
plt.xlabel( "x [UA]" )
plt.ylabel( "y [UA]" )
plt.legend(loc="upper left")
plt.axis("equal")
plt.savefig("grafica_opcional.png", dpi=3000)
plt.show()