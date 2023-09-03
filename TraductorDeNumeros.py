'''
Programa simple que traduce números del español al inglés.

Se define un diccionario llamado numerosTraducidos que contiene pares clave-valor.
Cada clave representa un número en español,
y el valor asociado es la traducción de ese número al inglés.

Se muestra un mensaje en la consola que le pide al usuario ingresar un número en español:
"Ingresa el número en español a traducir".

El programa espera a que el usuario introduzca un número en español
y almacena la entrada en la variable numeroEspanol mediante la función input().

Luego, el programa intenta buscar la traducción del número ingresado
en el diccionario numerosTraducidos utilizando numeroEspanol como clave.
Si la clave existe en el diccionario, imprimirá la traducción correspondiente en inglés;
de lo contrario, puede generar un error si el número no está en el diccionario.

En resumen, este programa permite al usuario ingresar un número en español y devuelve su traducción al inglés utilizando un diccionario predefinido. Por ejemplo, si el usuario ingresa "tres", el programa imprimirá "three".
'''


numerosTraducidos = {
    "uno":    "one",
    "dos":    "two",
    "tres":   "three",
    "cuatro": "four",
    "cinco":  "five",
    "seis":   "six",
    "siete":  "seven",
    "ocho":   "eight",
    "nueve":  "nine",
    "diez":   "ten"
}

print("Ingresa el número en español a traducir")
numeroEspanol = input()
if numeroEspanol in numerosTraducidos:
    print(numerosTraducidos[numeroEspanol])
else:
    print("No se encontró una traducción para '" + numeroEspanol + "'.")
