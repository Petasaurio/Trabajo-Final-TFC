# En este script se le realiza el metodo de la biseccion a la funcion 'kepler', para aproximar
# el angulo correspondiente a un tiempo dado. Si se desea realizar el metodo de la biseccion a
# otra funcion, se debera cambiar el codigo para importar al modulo y funcion correctas.

def biseccion(t, error):
    import math as m
    from coordenadas import kepler

    a= 0                            # definir arbitrariamente el intervalo de trabajo de la variable independiente
    b= 4/5*m.pi
    t_min = kepler(a)               # calculo el intervalo de trabajo de la variable dependiente
    t_max = kepler(b)

    if t <= t_min or t >= t_max:              # si se ingresa la variable dependiente fuera del intervalo de trabajo salta ERROR
        print("ERROR: por favor ingrese un tiempo dentro del intervalo de trabajo: ({}, {})".format(t_min,t_max))
    else:
        E=(b-a)/2
        c=(b+a)/2
        while E >= error:                     # metodo de la biseccion
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
