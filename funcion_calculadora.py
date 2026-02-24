print("========Mi Super Calculadora==========")
num_1 = float(input("Escriba el valor del primer numero: "))
num_2 = float(input("Escriba el valor del segundo numero: "))
operacion = input("¿Cual operacion deseas hacer? +, -, *, / -> ")

def calculadora(num_1, num_2, operacion):
    if operacion == "+":
        return num_1 + num_2
    elif operacion == "-":
        return num_1 - num_2
    elif operacion == "*":
        return num_1 * num_2
    elif operacion == "/":
        if num_2 != 0:
            return num_1 / num_2
        else:
            return "error division con 0"    
    else:
        return "error en la operacion"
    
resultado = calculadora(num_1, num_2, operacion) 
print("El resultado es:", resultado)
