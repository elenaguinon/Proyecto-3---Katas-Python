from functools import reduce
import math

#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

#Definimos la función
def frecuencia(texto):
    frecuencias = {}
#Recorremos con un bucle for siempre que el caracter no sea un espacio y sumamos la frecuencia de cada letra
    for letra in texto:
        if letra != " ":
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1

    return frecuencias

resultado = frecuencia("Que la fuerza te acompañe")
print(resultado)

# 2.Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().


lista_numeros = [5,10,15,20,25]             

# Creamos la funcion                             
def multiplicar(numero):                                         
    """Esta funcion multiplica por 2"""                                
    return numero *2                                                              

print(list(map(multiplicar, lista_numeros)))       

#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def palabras(lista, objetivo):
    # Creo una lista vacía para guardar las palabras encontradas
    resultado = []

    # Recorro cada palabra de la lista
    for palabra in lista:
        # Si la palabra objetivo está dentro de la palabra, la guardo
        if objetivo in palabra:
            resultado.append(palabra)

    # Devuelvo la lista con las palabras encontradas
    return resultado


#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
def diferencias(lista1, lista2):
    # Recorro las dos listas a la vez con map
    # A cada valor de la primera lista le resto el valor de la segunda
    return list(map(lambda x, y: x - y, lista1, lista2))


#5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado por defecto 5. La función debe calcular la media y determinar si la media es mayor o igual que nota_aprobado.
def calcular_media(notas, nota_aprobado=5):
    # Calculo la media de las notas
    media = sum(notas) / len(notas)

    # Compruebo si la media es suficiente para aprobar
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    # Devuelvo la media y el estado
    return media, estado


#6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(numero):
    # Si el número es 0, devuelvo 1 porque es el caso base
    if numero == 0:
        return 1

    # Multiplico el número por el factorial del número anterior
    return numero * factorial(numero - 1)


#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
def tuplas_a_strings(lista):
    # Con map convierto cada tupla en texto
    return list(map(lambda tupla: str(tupla), lista))


#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada.
def dividir_numeros():
    try:
        # Pido el primer número y lo convierto a decimal
        numero1 = float(input("Introduce el primer número: "))

        # Pido el segundo número y lo convierto a decimal
        numero2 = float(input("Introduce el segundo número: "))

        # Divido los dos números
        resultado = numero1 / numero2

        # Muestro el resultado
        print(resultado)

    except ValueError:
        # Este error aparece si el usuario no escribe un número
        print("Debes introducir números.")

    except ZeroDivisionError:
        # Este error aparece si el segundo número es 0
        print("No se puede dividir entre cero.")


#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. Usa la función filter().
def filtrar_mascotas(mascotas):
    # Guardo las mascotas que quiero excluir
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    # Uso filter para quedarme solo con las mascotas permitidas
    return list(filter(lambda mascota: mascota not in prohibidas, mascotas))


#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
class ListaVaciaError(Exception):
    pass


def promedio_lista(lista):
    try:
        # Compruebo si la lista está vacía
        if len(lista) == 0:
            raise ListaVaciaError("La lista está vacía.")

        # Calculo el promedio
        return sum(lista) / len(lista)

    except ListaVaciaError as error:
        # Muestro el error personalizado
        print(error)


#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado, maneja las excepciones adecuadamente.
def pedir_edad():
    try:
        # Pido la edad y la convierto a número entero
        edad = int(input("Introduce tu edad: "))

        # Compruebo que la edad esté dentro del rango correcto
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera de rango.")

        # Si todo está bien, muestro un mensaje
        print("Edad correcta.")

    except ValueError as error:
        # Muestro el error si la edad no es válida
        print(error)


#12. Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
def longitud_palabras(frase):
    # Separo la frase en palabras
    palabras = frase.split()

    # Uso map para calcular la longitud de cada palabra
    return list(map(lambda palabra: len(palabra), palabras))


#13. Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
def mayus_minus(caracteres):
    # Uso set para eliminar letras repetidas
    letras_unicas = set(caracteres)

    # Uso map para crear una tupla con mayúscula y minúscula
    return list(map(lambda letra: (letra.upper(), letra.lower()), letras_unicas))


#14. Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
def palabras_por_letra(lista, letra):
    # Uso filter para guardar solo las palabras que empiezan por la letra indicada
    return list(filter(lambda palabra: palabra.startswith(letra), lista))


#15. Crea una función lambda que sume 3 a cada número de una lista dada.
# Creo una lambda que recibe una lista
# Dentro uso map para sumar 3 a cada número
sumar_tres = lambda lista: list(map(lambda numero: numero + 3, lista))


#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
def palabras_largas(texto, n):
    # Separo el texto en palabras
    palabras = texto.split()

    # Uso filter para quedarme con las palabras más largas que n
    return list(filter(lambda palabra: len(palabra) > n, palabras))


#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
def lista_a_numero(lista):
    # Uso reduce para ir formando el número completo
    return reduce(lambda total, numero: total * 10 + numero, lista)


#18. Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.
# Creo una lista de estudiantes con nombre, edad y calificación
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 80},
    {"nombre": "Marta", "edad": 21, "calificacion": 90}
]

# Uso filter para guardar solo los estudiantes con calificación mayor o igual a 90
estudiantes_aprobados = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))


#19. Crea una función lambda que filtre los números impares de una lista dada.
# Creo una lambda que devuelve solo los números que no son divisibles entre 2
impares = lambda lista: list(filter(lambda numero: numero % 2 != 0, lista))


#20. Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
def solo_enteros(lista):
    # Uso filter para quedarme solo con los elementos de tipo int
    return list(filter(lambda elemento: type(elemento) == int, lista))


#21. Crea una función que calcule el cubo de un número dado mediante una función lambda.
# Creo una lambda que eleva el número a 3
cubo = lambda numero: numero ** 3


#22. Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
def producto_total(lista):
    # Uso reduce para multiplicar todos los números de la lista
    return reduce(lambda total, numero: total * numero, lista)


#23. Concatena una lista de palabras. Usa la función reduce().
def concatenar_palabras(lista):
    # Uso reduce para unir todas las palabras
    return reduce(lambda texto, palabra: texto + palabra, lista)


#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
def diferencia_total(lista):
    # Uso reduce para ir restando todos los números
    return reduce(lambda total, numero: total - numero, lista)


#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(texto):
    # Uso len para contar los caracteres del texto
    return len(texto)


#26. Crea una función lambda que calcule el resto de la división entre dos números dados.
# Creo una lambda que devuelve el resto de dividir a entre b
resto = lambda a, b: a % b


#27. Crea una función que calcule el promedio de una lista de números.
def promedio(lista):
    # Sumo todos los números y divido entre la cantidad de elementos
    return sum(lista) / len(lista)


#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    # Creo una lista para guardar los elementos que ya han aparecido
    vistos = []

    # Recorro cada elemento de la lista
    for elemento in lista:
        # Si el elemento ya estaba en vistos, es el primer duplicado
        if elemento in vistos:
            return elemento

        # Si no estaba, lo añado a vistos
        vistos.append(elemento)

    # Si no hay duplicados, devuelvo None
    return None


#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
def enmascarar(variable):
    # Convierto la variable a texto
    texto = str(variable)

    # Creo los símbolos # y dejo visibles los últimos cuatro caracteres
    return "#" * (len(texto) - 4) + texto[-4:]


#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    # Ordeno las letras de las dos palabras y las comparo
    return sorted(palabra1) == sorted(palabra2) and palabra1 != palabra2


#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
def buscar_nombre():
    # Pido varios nombres separados por comas
    nombres = input("Introduce nombres separados por comas: ").split(",")

    # Pido el nombre que quiero buscar
    nombre = input("Introduce el nombre a buscar: ")

    # Compruebo si el nombre está en la lista
    if nombre in nombres:
        print("Nombre encontrado.")
    else:
        raise ValueError("Nombre no encontrado.")


#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def buscar_empleado(nombre, empleados):
    # Recorro la lista de empleados
    for empleado in empleados:
        # Si encuentro el nombre, devuelvo su puesto
        if empleado["nombre"] == nombre:
            return empleado["puesto"]

    # Si no lo encuentro, devuelvo este mensaje
    return "La persona no trabaja aquí."


#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
# Uso map para sumar los elementos que están en la misma posición
sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))


#34. Crea la clase Arbol.
class Arbol:
    def __init__(self):
        # El tronco empieza con longitud 1
        self.tronco = 1

        # Las ramas empiezan como una lista vacía
        self.ramas = []

    def crecer_tronco(self):
        # Aumento el tronco en 1
        self.tronco += 1

    def nueva_rama(self):
        # Añado una rama nueva con longitud 1
        self.ramas.append(1)

    def crecer_ramas(self):
        # Aumento todas las ramas en 1
        self.ramas = list(map(lambda rama: rama + 1, self.ramas))

    def quitar_rama(self, posicion):
        # Quito la rama de la posición indicada
        self.ramas.pop(posicion)

    def info_arbol(self):
        # Devuelvo la información del árbol
        return self.tronco, len(self.ramas), self.ramas


# Creo un árbol
arbol = Arbol()

# Hago crecer el tronco
arbol.crecer_tronco()

# Añado una rama
arbol.nueva_rama()

# Hago crecer todas las ramas
arbol.crecer_ramas()

# Añado dos ramas más
arbol.nueva_rama()
arbol.nueva_rama()

# Quito la rama situada en la posición 2
arbol.quitar_rama(2)

# Guardo la información del árbol
info = arbol.info_arbol()


#35. Crea la clase UsuarioBanco.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        # Guardo el nombre del usuario
        self.nombre = nombre

        # Guardo el saldo del usuario
        self.saldo = saldo

        # Guardo si tiene cuenta corriente o no
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        # Si no tiene suficiente saldo, lanzo un error
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente.")

        # Resto la cantidad al saldo
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        # Si el otro usuario no tiene suficiente saldo, lanzo un error
        if cantidad > otro_usuario.saldo:
            raise ValueError("Saldo insuficiente.")

        # Resto el dinero al otro usuario
        otro_usuario.saldo -= cantidad

        # Sumo el dinero al usuario actual
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        # Sumo dinero al saldo
        self.saldo += cantidad


# Creo los dos usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# Agrego 20 al saldo de Bob
bob.agregar_dinero(20)

# Transfiero 80 de Bob a Alicia
alicia.transferir_dinero(bob, 80)

# Retiro 50 del saldo de Alicia
alicia.retirar_dinero(50)


#36. Crea una función llamada procesar_texto.
def contar_palabras(texto):
    # Separo el texto en palabras
    palabras = texto.split()

    # Creo un diccionario vacío
    diccionario = {}

    # Recorro las palabras
    for palabra in palabras:
        # Cuento cuántas veces aparece cada palabra
        diccionario[palabra] = diccionario.get(palabra, 0) + 1

    return diccionario


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    # Reemplazo una palabra por otra
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra_eliminar):
    # Separo el texto en palabras
    palabras = texto.split()

    # Elimino la palabra indicada
    palabras = list(filter(lambda palabra: palabra != palabra_eliminar, palabras))

    # Uno otra vez las palabras
    return " ".join(palabras)


def procesar_texto(texto, opcion, *args):
    # Si la opción es contar, cuento las palabras
    if opcion == "contar":
        return contar_palabras(texto)

    # Si la opción es reemplazar, sustituyo una palabra por otra
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])

    # Si la opción es eliminar, borro una palabra del texto
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])


#37. Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.
def momento_dia():
    # Pido la hora al usuario
    hora = int(input("Introduce la hora: "))

    # Compruebo en qué parte del día está esa hora
    if hora >= 6 and hora < 12:
        print("Es de día")
    elif hora >= 12 and hora < 20:
        print("Es de tarde")
    else:
        print("Es de noche")


#38. Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
def calificacion_texto(nota):
    # Compruebo el rango de la nota y devuelvo el texto correspondiente
    if nota >= 0 and nota <= 69:
        return "insuficiente"
    elif nota >= 70 and nota <= 79:
        return "bien"
    elif nota >= 80 and nota <= 89:
        return "muy bien"
    elif nota >= 90 and nota <= 100:
        return "excelente"
    else:
        return "nota no válida"


#39. Escribe una función que tome dos parámetros: figura y datos, una tupla con los datos necesarios para calcular el área de la figura.
def calcular_area(figura, datos):
    # Si la figura es rectángulo, multiplico base por altura
    if figura == "rectangulo":
        return datos[0] * datos[1]

    # Si la figura es círculo, uso pi por radio al cuadrado
    elif figura == "circulo":
        return math.pi * datos[0] ** 2

    # Si la figura es triángulo, multiplico base por altura y divido entre 2
    elif figura == "triangulo":
        return datos[0] * datos[1] / 2

    # Si no coincide con ninguna figura, devuelvo un mensaje
    else:
        return "Figura no válida"


#40. Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento.
def precio_final():
    # Pido el precio original
    precio = float(input("Introduce el precio original: "))

    # Pregunto si tiene cupón
    cupon = input("¿Tienes cupón? sí/no: ")

    # Si tiene cupón, pido el descuento
    if cupon == "sí" or cupon == "si":
        descuento = float(input("Introduce el descuento: "))

        # Si el descuento es válido, lo resto al precio
        if descuento > 0:
            precio = precio - descuento

    # Muestro el precio final
    print("Precio final:", precio)

