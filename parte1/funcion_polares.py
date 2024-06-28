#este script crea una tabla con el radio en funcion del angulo para un perihelio dado y angulos entre -3pi/4 y 3pi/4
import math as m

RP = float(input("Ingrese el radio del periohelio (en UA): "))        # Ingresar por teclado el perihelio de la trayectoria a analizar

fichero = open("tabla_polares.dat", "w")
fichero.write("Tabla del radio en funcion del angulo para trayectoria parabolica de perihelio {} UA:\n   Angulo [rad]\t\t\t\t Radio [UA]\n".format(RP))

theta = -3/4*m.pi                                     #valor inicial de theta

while theta <= 3/4*m.pi:                              #iteraciones con sentencia while para calcular los radios y escribirlos en el fichero en funcion de los ángulos
    r = 2*RP/(1+m.cos(theta))
    fichero.write("{}\t\t\t{}\n".format(theta, r))
    theta += 0.005

fichero.close()