import matplotlib.pyplot as plt
import math as m
import graficadora as g

def menu():
    print("¿Qué desea realizar?")
    print("\t(0) Salir.\n")
    print("\tParte 1)")
    print("\t\t(a) Graficar la trayectoria del cometa junto a la órbita de la Tierra.")
    print("\t\t    (para el valor observado por Herschel de RP)")
    print("\t\t(b) [Opcional] Graficar las posibles trayectorias del cometa")
    print("\t\t    junto a la órbita de la Tierra. (para los valores")
    print("\t\t    de RP: 0,1; 0,25; 0,5; 0,75; 1 UA)\n")
    print("\tParte 2)")
    print("\t\t(c) Graficar la trayectoria del cometa junto a la órbita de la Tierra, con")
    print("\t\t    las posiciones destacadas del cometa 1, 2, y 3 meses después del perihelio.")
    print("\t\t    (para el valor observado por Herschel de RP)")
    print("\t\t(d) [Opcional] Graficar las posibles trayectorias del cometa")
    print("\t\t    junto a la órbita de la Tierra. (para los valores")
    print("\t\t    de RP: 0,1; 0,25; 0,5; 0,75; 1 UA)\n")
    return input("\t\t---> ")

sel = 1 # valor arbitrario e inicial para la seleccion
while sel != "0":
    sel = menu()
    if sel == "a":
        g.graficaParte1(0)
    elif sel == "b":
        g.graficaParte1(1)
    elif sel != "0":
        print("No se reconoce la opcion!!")
        