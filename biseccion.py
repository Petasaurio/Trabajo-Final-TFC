#la funcion a analizar debe ser ingresada, este script solo le hace la biseccion
import math as m
from funcion_kepler import kepler

t=float(input("Ingrese el tiempo (en segundos) en el que desea saber la posicion del cometa: "))

a= -3/4*m.pi                            #defino arbitrariamente el intervalo donde se va a trabajar
b=  3/4*m.pi
tiempo_min = kepler(a)
tiempo_max = kepler(b)

if t <= tiempo_min or t >= tiempo_max:
    print("ERROR: por favor ingrese un tiempo dentro del intervalo ({}, {})".format(tiempo_min,tiempo_max))
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
    print(kepler(c-E) , kepler(c) , kepler(c+E))
    print("Las coordendas x e y del punto buscado son: ({} , {})UA".format(x,y))
