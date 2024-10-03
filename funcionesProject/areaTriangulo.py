#ejemplo para calcular el area del triangulo

#variables de entrada

base = int(input( "Ingrese la base: " ))
altura = int(input( "Ingrese la altura: " ))

#proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return  area

#invocar la funcion

resultado = calcularAreaTriangulo(base,altura)


#Salida

print(f" el areadel triangulo cuya base {base} y altura {altura} es: {resultado}")


# funcion con argumentos predeterminados

def my_function(country = "Colombia"):
    print("I am from " + country)

#invocar la funcion
my_function()
my_function( "Swenden" )

#argumentos arbitrarios

def mostrarEstudiantes(*args):
    print("El estudiante: " + args[2])

mostrarEstudiantes("Emil", "tobias", "linus")


#argumentos clave valor

def mostrarCarros(carro1, carro2,carro3):
    print("El carro es:" + carro2)

    mostrarCarros(carro1 = "BMW", carro3 = "Ferrari", carro2 = "Ford")

#Argumento **KWARGS

def mostrarCliente(**kwargs):
    print("Su apellido es :" kwargs["Apellido"])


    mostrarCliente(nombre = "tobias", apellido = "Refsnes")


#Declaracion de paso

def mifuncion():
    pass


#funciones integradas

x = min(5,10,25)
y = max(5,10,25)

print(x)
print(y)

#funciones integradas

num1 = pow(7, 4)

print(num1)

#modulo de matematicas

import math

num2 = math.sqrt(34)

print(num2)

#modulo de matematicas

import math

num3 = math.ceil(7.8)
num4 = math.floor(7.8)

print(num3) #returns 8
print(num4) #returns 7