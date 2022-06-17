# Impresión en pantalla print('Hola desde la consola')

print('Hola desde la consola')

# Operacion basica

sum = 1 + 2 # 3
product = sum * 2
print(product)

#Tipos de datos

planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

#Entrada de datos

print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

#Calculadora

print('Ingresa dos numeros')
num1 = input('Numero 1: ')
num2 = input('Numero : ')
sum = int(num1) + int(num2)
print('La suma es: ' + str(sum))

#Practica de convercion a unidades

print('Convertidor')
parsec = input('Ingrese los parsec: ')

lightyears = 3.26156 * float(parsec)

print(str(parsec) + " parsec, is " + str(lightyears) + " lightyears")
