import Ejercicio1
op=int(input("1. Tabla \n2. Area de un Cuadrado \n3. Operaciones \n¿Que funcion desea utilizar?: "))
if op==1:
    numero=int(input("Ingrese el numero de la tabla: "))
    Ejercicio1.tabla(numero)

elif op==2:
    lado=int(input("Ingrese el lado del cuadrado: "))
    Ejercicio1.area_cuadrado(lado)

elif op==3:
    opcion=int(input("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n¿Qué desea hacer?: "))
    num1=float(input("Ingrese el primer número: "))
    num2=float(input("Ingrese el segundo número: "))
    Ejercicio1.operaciones(opcion, num1, num2)
