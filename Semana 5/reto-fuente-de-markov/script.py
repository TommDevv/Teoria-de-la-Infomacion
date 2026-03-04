#Realizado por Tomás Alejandro Delgado Ortíz - 20221020045
# Reto Fuente de Markov
# Para el ejercicio se implementa una lista de palabras en español de aproximadamente 70000 palabras encontrado en internet,
# esta es la fuente de la que se tomaron las palabras: https://github.com/xavier-hernandez/spanish-wordlist/blob/main/text/spanish_words.txt

data= "./spanish_words.txt"

words = []

guessword = ['_', '_', '_', '_']

letters = {
    "a": 0.0,
    "b": 0.0,
    "c": 0.0,
    "d": 0.0,
    "e": 0.0,
    "f": 0.0,
    "g": 0.0,
    "h": 0.0,
    "i": 0.0,
    "j": 0.0,
    "k": 0.0,
    "l": 0.0,
    "m": 0.0,
    "n": 0.0,
    "ñ": 0.0,
    "o": 0.0,
    "p": 0.0,
    "q": 0.0,
    "r": 0.0,
    "s": 0.0,
    "t": 0.0,
    "u": 0.0,
    "v": 0.0,
    "w": 0.0,
    "x": 0.0,
    "y": 0.0,
    "z": 0.0,
}

#Se filtran las palabras de unicamente 4 letras, y se guardan en una lista

with open(data, encoding="latin-1") as f:
    for linea in f:
        palabra = linea.strip()
        if len(palabra) == 4:
            words.append(palabra)
        else:
            pass

#Se definen las probabilidades de cada letra de acuerdo a su ratio de aparicion en en las palabras del diccionario
def definir_probabilidades():
    for letra in letters:
        count = 0
        for palabra in words:
            if letra in palabra:
                count += 1
        letters[letra] = count / len(words)

#Se selecciona la letra con mayor probabilidad de aparecer en las palabras restantes del diccionario
def seleccionar_letra():
    return max(letters, key=letters.get)

#Actualiza las probabilidades de cada letra basandose en las palabras ya adivinadas y la respectiva 
#combinacion de cada letra con las ya adivinadas
def actualizar_probabilidades(guessword):
    for letra in letters:
        if letters[letra] == 0.0:
            continue
        count = 0.0
        for palabra in words:
            if all(guessword[i] == palabra[i] for i in range(len(guessword)) if guessword[i] != "_") and letra in palabra:
                count += 1
        letters[letra] = count / len(words) if len(words) > 0.0 else 0.0
                

definir_probabilidades()


# Simulación del juego Ahorcado
print("========================================")
print("           JUEGO DEL AHORCADO          ")
print("========================================")
print()
print("El programa intentará adivinar una palabra de cuatro letras." \
"nResponde con 's' si la letra está en la palabra y 'n' si no lo está." \
"nSi la letra está en la palabra, ingresa las posiciones de la letra (0-3) separadas por comas.")
print()
print("Palabra a adivinar:", guessword)
print()

attempts = 0
while "_" in guessword:
    attempts += 1

    letra = seleccionar_letra()
    respuesta = input(f"¿La letra {letra} está en la palabra? (s/n): ").strip().lower()
    #Si la letra está en la palabra oregunta en que posiciones para almacenar las letras
    #adivinadas y buscar la coincidencia
    if respuesta == "s":
        posiciones = input("Ingrese las posiciones de la letra (0-3) separadas por comas: ")
        for pos in posiciones.split(","):
            pos = int(pos.strip())
            guessword[pos] = letra
        letters[letra] = 0.0
        actualizar_probabilidades(guessword)
        print("Palabra a adivinar:", guessword)
        print()
    else:
        letters[letra] = 0.0
        print("Palabra a adivinar:", guessword)
        print()

print("Palabra adivinada:", "".join(guessword))
print("Número de intentos:", attempts)

