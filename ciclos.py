#1. Imprimir todos los múltiplos de 3 que hay entre 1 y 100.
print("")
print ("1.Imprimir todos los múltiplos de 3 que hay entre 1 y 100.")
multiplo=3
while multiplo<101:
    print(multiplo)
    multiplo+=3


#2. Imprimir los números impares entre 0 y 100
print("")
print("2. Imprimir los números impares entre 0 y 100")
impar=3
while impar<101:
    print(impar)
    impar+=2




#3. Imprimir los números pares del 1 al 100
print("")
print("3. Imprimir los números pares del 1 al 100")
par=2
while par<101:
    print(par)
    par+=2


#4. Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30.
print("")
print("4. Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30")
num=1
while num<31:
    cuadrados=num**2
    print(cuadrados)
    num += 1


#5. Escribir un programa que sume los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla
print("")
print(" 5. Escribir un programa que sume los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla")

def sumadecuadrados(n):
    suma = 0
    for x in range(1, n+1):
        suma += x**2
    return suma

resultado = sumadecuadrados(100)
print("La suma de las potencias de los primero 100 numeros es:", resultado)

#6. Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente
print("")
print("6. Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente")



def numerosentre(a, b):
    for x in range(a+1, b):
        print(x, end=" ")

a = int(input("Ingrese el primer numero "))
b = int(input("Ingrese el segundo numero mayor al primero: "))

if a>= b:
    print("El primer número debe ser menor que el segundo.")
else:
    print("Los números comprendidos entre", a, "y", b, "son:")
    numerosentre(a,b)

#7. Sumar todos los números que se digitan por teclado mientras no sea cero
print("")
print("7. Sumar todos los números que se digitan por teclado mientras no sea cero")

def sumanumeros():
    suma = 0
    while True:
        a = float(input("Ingrese un número y cuando quiera terminar de sumar digite 0: "))
        if a == 0:
            break
        suma += a
    return suma

resultado = sumanumeros()
print("La suma de los números ingresados es:", resultado)