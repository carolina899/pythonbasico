# loops 
mi_lista = [1,2,3,4,5]

for i in mi_lista:
    print("el numero es:",i)

resultado = 0
for i in mi_lista:
    resultado += i

print(f"el resultado de la suma de mi lista es:{resultado}")


for i in range (2, 9):
    print(i)


mi_lista_2 = ["LUNES","MARTES","MIERCOLES","VIERNES"]
for i in mi_lista_2:
    if i !="lunes":
        print(f"feliz{i}!")

#while loop
i= 0

while i < 5:
    i += 1
    if i==3:
        continue
    print(i)
else:
    print("i es ahora mayor o igual a 5")



  #practica 2
    # dada la lista  mi_lista = ["lunes","martes","miercoles","jueves","viernes"]
    # imprimir cada elemento de la lista 3 veses y cuando sea lunes no lo incluyas
    # pista: usa los dos tipos loops while y for en el mismo programa para lograrlo
    # resultado:
    # martes
    # miercoles
    # jueves
    # viernes
    # martes
    # miercoles
    # jueves
    # viernes
    # martes
    # miercoles
    # jueves
    # viernes
    i= 0
mi_lista_2 = ["LUNES","MARTES","MIERCOLES","JUEVES","VIERNES"]
while i < 3:
    i += 1
    for d in mi_lista_2:
        if d!="LUNES":
            print(d) 