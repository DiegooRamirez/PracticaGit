def tabla(numero):
    for i in range (1,11):
        print(f"{numero} x {i} = {numero*i}")
        i=+1

def area_cuadrado(lado):
    print(f"El area es: {lado*lado}")

def operaciones(op, num1, num2):
    if op==1:
        print(f"El resultado es: {num1+num2}")
    elif op==2:
        print(f"El resultado es: {num1-num2}")
    elif op==3:
        print(f"El resultado es: {num1*num2}")
    elif op==4:
        print(f"El resultado es: {num1/num2}") 
