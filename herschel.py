# Desde este menu se administran las funciones y programas del trabajo.
# Ejecute y seleccione la opcion deseada.
# Los archivos seran guardados en las carpetas correspondientes.

import graficadora as g

def menu():
    print("¿Qué desea realizar?")
    print("\t\t(0) Salir.\n")
    print("\tParte 1)")
    print("\t\t(a) Crear tablas de coordenadas polares y cartesianas del cometa,")
    print("\t\t    y graficar su trayectoria junto a la órbita de la Tierra.")
    print("\t\t    (para el valor observado por Herschel de RP)")
    print("\t\t(b) [Opcional] Crear tablas de coordenadas polares y cartesianas para")
    print("\t\t    hipoteticos cometas con distintos valores de RP y graficar sus")
    print("\t\t    trayectorias junto a la órbita de la Tierra y la del cometa C/1823 Y1.")
    print("\t\t    (valores hipoteticos de RP usados: 0,1 ; 0,25 ; 0,5 ; 0,75 ; 1 UA)\n")
    print("\tParte 2)")
    print("\t\t(c) Calcular el angulo θ y las coordenadas x e y del cometa para")
    print("\t\t    1, 2 y 3 meses luego del perihelio. Graficar la trayectoria del cometa")
    print("\t\t    junto a la órbita de la Tierra y las 3 posiciones destacadas.")
    print("\t\t    (usando el valor observado por Herschel de RP)")
    print("\t\t(d) [Opcional] Crear tabla con valores de x e y para distintos tiempos")
    print("\t\t    entre 0 y 3 meses y graficar resultados en el plano xy junto a la órbita terrestre")
    return input("\t\t---> ")

sel = 1                 # valor arbitrario e inicial para la seleccion
while sel != "0":
    sel = menu()
    if sel == "0":
        print("Cerrando programa...\n")
        break
    elif sel == "a":
        g.graficar(1)
    elif sel == "b":
        g.graficar(2)
    elif sel == "c":
        g.graficar(3)
    elif sel =="d":
        g.graficar(4)
    else:
        print("ERROR: No se reconoce la orden.\n")
    print("Reiniciar...")
        