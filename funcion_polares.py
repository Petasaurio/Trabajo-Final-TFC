import math as m

RP = 0.22674        # Radio del perihelio en UA
PI=m.pi
theta = -3/4*PI
r = 0

fichero = open("tabla_polares.dat", "w")
fichero.write("Tabla de radios en funcion del angulo para trayectoria parabolica de perihelio {} UA:\n Angulo [rad]\t\t Radio [UA]\n".format(RP))

while theta <= 3/4*PI:
    r = 2*RP/(1+m.cos(theta))
    fichero.write("{} \t {}\n".format(theta, r))
    theta += 0.005

fichero.close()