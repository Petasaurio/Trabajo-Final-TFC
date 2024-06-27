def kepler(theta):
    import math as m

    RP=0.22674*1.496E11             #conversion de RP de UA a m
    G=6.67E-11                      #constante de gravitacion universal en [N m^2 kg^-2]
    M=1.989E30                      #masa del sol en [kg]


    VP= m.sqrt(2*G*M/RP)                    #velocidad en el perihelio en m/s
    K=(G**2)*(M**2)/(RP**3)/(VP**3)         #constante K

    t=( m.tan(theta/2)**3 + 3*m.tan(theta/2) ) / (6*K)
    return t
