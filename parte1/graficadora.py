#este script lee el archivo tabla_cartesianas.dat y crea una grafica que incluye: la trayectoria del cometa, de la Tierra y la posicion del sol
import matplotlib.pyplot as plt
import math as m

fichero = open("tabla_cartesianas.dat", "r")        #abrir archivo de datos para su lectura

lista = fichero.readlines()

lista_x = []
lista_y = []

for i in range(2, len(lista)):              #iteraciones con sentencia for para guardar la informacion del archivo en lista_x y lista_y
    fila = lista[i].split()

    lista_x.append( float(fila[0]) )
    lista_y.append( float(fila[1]) )

fichero.close()

lista_xtierra=[]
lista_ytierra=[]
theta=0

while theta <= 2*m.pi:                      #iteraciones con sentencia while para crear listas con las coordenadas de la orbita terrestre
    lista_xtierra.append( m.cos(theta) )
    lista_ytierra.append( m.sin(theta) )
    theta += 0.005

plt.plot(lista_x, lista_y, label="Trayectoria del cometa C/1823 Y1")            #uso de matplotlib para crear las 3 trayectorias (cometa, tierra y sol)
plt.plot(lista_xtierra, lista_ytierra, color="red", linestyle="dashed", label="Orbita de la tierra")
plt.scatter([0], [0], marker="o", s=100, color="#FFC714")

plt.grid()                      #configuracion de detalles para pulir la grafica
plt.title("Trayectoria del cometa C/1823 Y1 y la orbita de la Tierra")
plt.xlabel( "x [UA]" )
plt.ylabel( "y [UA]" )
plt.legend(loc="upper left")
plt.axis("equal")
plt.savefig("grafica.png", dpi=3000)
plt.show()