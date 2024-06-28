#en este script se le realiza el metodo de la biseccion a la funcion kepler para aproximar el angulo correspondiente a un tiempo dado
#si se desea realizar el metodo de la biseccion a otra funcion, se debera cambiar el codigo para importar al modulo y la funcion correctas
import math as m
from funcion_kepler import kepler

t=float(input("Ingrese el tiempo (en segundos) en el que desea saber la posicion del cometa (1mes = 2592000s): "))

a= -3/4*m.pi                            #defino arbitrariamente el intervalo donde se va a trabajar
b=  3/4*m.pi
tiempo_min = kepler(a)
tiempo_max = kepler(b)

if t <= tiempo_min or t >= tiempo_max:
    print("ERROR: por favor ingrese un tiempo dentro del intervalo de trabajo: ({}, {})".format(tiempo_min,tiempo_max))
else:
    error=float(input("Ingrese el error con el que quiere obtener el resultado: "))

    E=(b-a)/2
    c=0
    while E >= error:                 #metodo biseccion
        if (kepler(c)-t) == 0:
            E=0
            break
        elif (kepler(a)-t)*(kepler(c)-t) < 0:
            E=(b-a)/2
            b=c
            c=(b+a)/2
        else:
            E=(b-a)/2
            a=c
            c=(b+a)/2

    RP=0.22674
    r = 2*RP/(1+m.cos(c))
    x = (-1)*r*m.cos(c)
    y =      r*m.sin(c)
    
    print()
    print("El angulo buscado es {} , y fue obtenido con un error de {}".format(c,E))
    print(kepler(c-E) , kepler(c) , kepler(c+E))    #acá muestro el intervalo de tiempos que obtengo de la aproximación para verificar que el t ingresado cae en ese intervalo
    print("Las coordendas x e y del punto buscado son: ({} , {}) UA".format(x,y))
