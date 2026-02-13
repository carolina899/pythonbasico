# numericos y flotantes
print(int(7))
print(float(7.7))
print(type(7))
print(type(7.77))
print(int(1+2))
print(int(10*2))
print("===== operadores matematicos=======")
#+
#-
#*
#/
#**
# % modulo

print(int(2**3))
print(int(4**8))
print(float(10%2))
print(float(25%4))

ventas = 199999
print("nuestras ventas fueron : ", ventas)

is_active = True
print (bool(is_active))


game_over = False
print(game_over)
edad = 16
if (edad>18):
    print("si puedo entrar a el bar!")
else:
    print("no puedo entrar a el bar!")


mi_numero = int(input("¿cual es el numero que deseas verificar?:"))
print(f"el numero que deseas verificar es {mi_numero}")
if mi_numero % 2 == 0 :
    print(f"el numero {mi_numero} es par!!!")
else:
    print(f"el numero {mi_numero} es impar!!")