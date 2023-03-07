import math

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

d=(b*b)-4*a*c
if d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)

    print("-----------soluciones----------")
    print("solucion x1 : ",x1)
    print("solucion x2 : ",x2)
elif d == 0:
    
    r=-b+math.sqrt(d)/(2*a)
    print("la solucion de la ecuacion es unica")
    print("x = ", r)
else:
    print("La ecuacion no posee solucion real")