sum1 = 30
sum2 = 3
sum3 = 40
sum4 = 15

resultado = sum1 + sum2
print(resultado)

resultado2 = sum1 * sum2 
print(resultado2)

resultado3 = sum1 / sum2 
print (resultado3)

resultado4 = resultado / resultado3
print ( resultado4)

resultado5 = (sum1 + sum3) * sum2 / sum4
print (resultado5)

def suma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado
print(f"el resultado es : {suma(1, 4)}")

numeros = [1,2,3,4]
for numero in numeros:
    # print(f"ciclo for {numero}")

    i = 0

while i < len(numeros):
    print(f"ciclo while {numeros[i]}")
    i += 1

edad = 20

if edad > 18:
    print("eres mayor de edad")
else:
    print("no eres mayor de edad") 

golesArgentina = 2
golesFrancia = 0

if golesArgentina > golesFrancia:
    print("gana Argentina")
elif golesFrancia > golesArgentina:
    print("Gana Francia")
else:
    print("Empate")

persona = {
    "nombre": "fulano",
    "edad": "10",
    "ciudad": "vdr"
}

persona["nacionalidad"] = "Argentina"

print(f"el nombre es: {persona['nombre']}")
print(f"la edad es: {persona['edad']}")
print(f"la nacionalidad es: {persona['nacionalidad']}")
print(f"la ciudad de origen es:{persona['ciudad']}")

with open("mi.txt", "w") as archivo:
    archivo.write("hola mundo")

with open("mi.txt", "w") as archivo:
    texto = archivo.read()
    print(f"el texto es: {texto}")

palabra = "tal"

with open("mi.txt", "r") as archivo:
    lineas = []
    for linea in archivo:
        if palabra in linea:
            print(f"encontro: {palabra}")
        else:
            print("error")

# fizz buzz

for i in range(1, 100):
    if i % 3 == 0:
        print("fizz") 
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)  

# sum1 = 1
# sum2 = 1
# resultado = sum1 + sum2
# print(resultado)

def suma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado
# print(f"el resultado es : {suma(1, 4)}")

numeros = [1,2,3,4]
for numero in numeros:
    # print(f"ciclo for {numero}")

    i = 0

while i < len(numeros):
    print(f"ciclo while {numeros[i]}")
    i += 1

edad = 20

if edad > 18:
    print("eres mayor de edad")
else:
    print("no eres mayor de edad") 

golesArgentina = 2
golesFrancia = 0

if golesArgentina > golesFrancia:
    print("gana Argentina")
elif golesFrancia > golesArgentina:
    print("Gana Francia")
else:
    print("Empate")

persona = {
    "nombre": "fulano",
    "edad": "10",
    "ciudad": "vdr"
}

persona["nacionalidad"] = "Argentina"

print(f"el nombre es: {persona['nombre']}")
print(f"la edad es: {persona['edad']}")
print(f"la nacionalidad es: {persona['nacionalidad']}")

with open("mi.txt", "w") as archivo:
    archivo.write("hola mundo")

with open("mi.txt", "w") as archivo:
    texto = archivo.read()
    print(f"el texto es: {texto}")

palabra = "tal"

with open("mi.txt", "r") as archivo:
    lineas = []
    for linea in archivo:
        if palabra in linea:
            print("encontro")
        else:
            print("encontro")

# sum1 = 1
# sum2 = 1
# resultado = sum1 + sum2
# print(resultado)