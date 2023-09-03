'''
Este código en Python está creando un diccionario llamado estudiantes
y luego realizando algunas operaciones con él.
Aquí está una descripción paso a paso:

Se crea un diccionario vacío llamado estudiantes utilizando llaves {}.

Se agregan varios pares clave-valor al diccionario estudiantes.
Cada clave es un número de identificación (generalmente un número único o código)
y el valor es el nombre de un estudiante asociado a esa identificación.

"111" está asociado a "Bart Simpson".
"222" está asociado a "Lisa Simpson".
"333" está asociado a "Nelson Muntz".
"41" está asociado a "Milhouse Van Houten".
"9" está asociado a "Rafa Gorgory".

Se imprime la cantidad de elementos en el diccionario estudiantes
utilizando la función len(estudiantes).
Esto mostrará cuántos estudiantes están registrados en el diccionario.

Se imprime el estudionte con el identificador "222" asociado a "Lisa Simpson"
'''

estudiantes = {}

estudiantes["777"] = "Bart Simpson"
estudiantes["222"] = "Lisa Simpson"
estudiantes["333"] = "Nelson Muntz"
estudiantes["41"] = "Milhouse Van Houten"
estudiantes["9"] = "Rafa Gorgory"

# Se imprime la cantidad de estudiantes:
print(len(estudiantes))

# Se imprime el estudiante con la identificación "222":
print(estudiantes["222"])

if "1000" in estudiantes:
    print(estudiantes["1000"])
else:
    print("No existe un estudiante con el identificador '1000'")
