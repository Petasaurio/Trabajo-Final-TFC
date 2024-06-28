#en este script se le realiza el metodo de la biseccion a la funcion 'kepler' para aproximar el angulo correspondiente a un tiempo dado
#si se desea realizar el metodo de la biseccion a otra funcion, se debera cambiar el codigo para importar al modulo y la funcion correctas
def biseccion(t, error):
    import math as m
    from coordenadas import kepler

    a= 0                            #definir arbitrariamente el intervalo de trabajo de la variable independiente
    b= 4/5*m.pi
    t_min = kepler(a)          #calculo el intervalo de trabajo de la variable dependiente
    t_max = kepler(b)

    if t <= t_min or t >= t_max:              #si se ingresa la variable dependiente fuera del intervalo de trabajo salara ERROR
        print("ERROR: por favor ingrese un tiempo dentro del intervalo de trabajo: ({}, {})".format(t_min,t_max))
    else:
        E=(b-a)/2
        c=(b+a)/2
        while E >= error:                 #metodo biseccion
            if (kepler(c)-t) == 0:
                E=0
                break
            elif (kepler(a)-t)*(kepler(c)-t) < 0:
                b=c
                c=(a+b)/2
                E=(b-a)/2
            else:
                a=c
                c=(a+b)/2
                E=(b-a)/2

        return [c,E]
        
        
        
        RP=0.22674
        r = 2*RP/(1+m.cos(c))
        x = (-1)*r*m.cos(c)
        y =      r*m.sin(c)
    
        print()
        print("El angulo buscado es {} , y fue obtenido con un error de {}".format(c,E))
        print(kepler(c-E) , kepler(c) , kepler(c+E))    #acá muestro el intervalo de tiempos que obtengo de la aproximación para verificar que el t ingresado cae en ese intervalo
        print("Las coordendas x e y del punto buscado son: ({} , {}) UA".format(x,y))
