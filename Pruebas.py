import Ejercicio1
op=int(input("1. Tabla \n2. Area de un Cuadrado \n3. Operaciones \n¿Que funcion desea utilizar?: "))
if op==1:
    numero=int(input("Ingrese el numero de la tabla: "))
    Ejercicio1.tabla(numero)
if op==2:
    lado=int(input("Ingrese el lado del cuadrado: "))
    Ejercicio1.area_cuadrado(lado)