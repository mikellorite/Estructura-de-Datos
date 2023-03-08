import os
import json
import random
from dibj import dibujo
import time

def limpiar_pantalla():
    os.system("cls" if os.name=="nt" else "clear")


nombre_archivo_palabras = "./lista.txt"
data = ""
if os.path.exists(nombre_archivo_palabras):
    with open(nombre_archivo_palabras) as f:
        data = json.load(f)

def menu_cambiar_lista():
    print('1: Añadir palabra')
    print('2: Eliminar palabra')
    print('3: Añadir categoria')
    print('4: Eliminar categoría')
    print('5: Guardar json')
    print('6: Atrás')
    decision = input('¿Qué quieres cambiar?: ')
    limpiar_pantalla()
    cambiar_lista(decision)

def cambiar_lista(n):
    if n == '1':
        time.sleep(1)
        return añadir_palabra()
    elif n == '2':
        time.sleep(1)
        return eliminar_palabra()
    elif n == '3':
        time.sleep(1)
        return añadir_categoria()
    elif n == '4':
        time.sleep(1)
        return eliminar_categoria()
    elif n == '5':
        time.sleep(1)
        return guardar_json()
    elif n == '6':
        limpiar_pantalla()
        time.sleep(1)
    else:
        limpiar_pantalla()
        time.sleep(1)
        print('Has escrito mal. Íntentalo de nuevo')
        return menu_cambiar_lista()

def añadir_palabra():
    print('CATEGORIAS:')
    for key in data:
        print(key)
    categoria = input("En que categoria quieres añadir: ")
    if categoria in data:
        palabra = input("Que palabra quieres añadir: ")
        data[categoria].append(palabra)
        limpiar_pantalla()
        time.sleep(1)
        menu_cambiar_lista()
    else:
        print('Has escrito mal la categoria, intentelo de nuevo')
        añadir_palabra()

def eliminar_palabra():
    print('CATEGORIAS:')
    for key in data:
        print(key)
    categoria = input("En que categoria quieres eliminar una palabra: ")
    if categoria in data:
        print('PALABRAS DE TU CATEGORIA: ')
        for values in data[categoria]:
            print(values)
        palabra = input("Elimine la palabra que quieras: ")
        if palabra in data[categoria]:
            data[categoria].remove(palabra)
            limpiar_pantalla()
            time.sleep(1)
            menu_cambiar_lista()
        else:
            print('Has escrito mal la palabra, intentelo de nuevo')
            limpiar_pantalla()
            time.sleep(1)
            eliminar_palabra()
    else:
        limpiar_pantalla()
        time.sleep(1)
        print('Has escrito mal la categoria, intentelo de nuevo')
        eliminar_palabra()

def añadir_categoria():
    nueva_categoria = input("Dame categoria nueva: ")
    data[nueva_categoria] = []
    limpiar_pantalla()
    time.sleep(1)
    menu_cambiar_lista()

def eliminar_categoria():
    print('CATEGORIAS: ')
    for key in data:
        print(key)
    categoria = input('Qué categoria quiere eliminar: ')
    if categoria in data:
        del data[categoria]
        limpiar_pantalla()
        time.sleep(1)
        menu_cambiar_lista()
    else:
        print('Has escrito mal la categoria, intentelo de nuevo')
        limpiar_pantalla()
        time.sleep(1)
        eliminar_categoria()

def guardar_json():
    with open(nombre_archivo_palabras, 'w') as file:
        json.dump(data, file, indent=4)
    limpiar_pantalla()
    time.sleep(1)
    menu_cambiar_lista()

def elige_palabra():
    print('CATEGORIAS: ')
    for key in data:
        print(key)
    cat = input('Qué categoria?: ')
    if cat in data:
        j = random.randint(0, len(data[cat])-1)
        palabra = data[cat][j]
        return palabra
    else:
        print('Has escrito mal, inténtalo de nuevo')
        elige_palabra()

# 1: se le da una lista con letras dichas y la palabra a resolver
def muestre_ahorcado(letras, pal):
    incognita = ''
    for letra in pal:  # 2: cada letra de la palabra a resolver
# 3.1: no se ha dicho la letra y no es espacio --> _
        if letra != ' ' and letra not in letras:
            incognita += '_'
# 3.2: es espacio
        elif letra == ' ':
            incognita += ' '
# 3.3: se ha dicho la letra
        elif letra in letras:
            incognita += letra
    return incognita

def resolver(preg):
    yes = ['si', 'sí', 'SÍ', 'SI', 'resolver', 'Resolver', 'RESOLVER']
    if preg in yes:
        return True
    else:
        return False

def decide_nivel(n):
    if n == '1':
        return 10
    elif n == '2':
        return 7
    elif n == '3':
        return 5
    else:
        print('has escrito mal el nivel, inténtelo de nuevo', ahorcado())

def volver_a_jugar(p):
    if resolver(p):
        limpiar_pantalla()
        time.sleep(1)
        ahorcado()
    else:
        limpiar_pantalla()
        time.sleep(1)


def ahorcado():
    letras = []
    palabra_elegida = elige_palabra()
    Sigue = True
    cont = 0
    print('1: NIVEL FÁCIL')
    print('2: NIVEL MEDIO')
    print('3: NIVEL DIFÍCIL')
    nivel=input('¿Qué nivel quieres?')
    numnivel=decide_nivel(nivel)
    while Sigue:
        incognita = muestre_ahorcado(letras, palabra_elegida)
# se imprime la guia de la palabra y se informa de las letras utilizadas y de las vidas disponibles
        print('PALABRA',incognita)
        print('Tus letras utilizadas: ', letras)
        print('Te quedan ', numnivel-cont, 'intentos')
        dibujo(10-numnivel+cont)
# se pregunta si quiere resolver (terminaria el juego)
        pregunta = input('¿Quieres resolver?')
        if resolver(pregunta):
            if input('¿Qué palabra crees que es?: ') == palabra_elegida:
                print('CORRECTO!!! la palabra era: ', palabra_elegida)
            else:
                print('HAS FALLADO. La palabra era: ', palabra_elegida)
                dibujo(10)
            Sigue = False
# si no quiere resolver, sigue diciendo letras
        else:
            l = input('Di la siguiente letra: ')
            if l[0] in palabra_elegida and l[0] not in letras:    #si acierta letra, no se le quita vida
                cont-=1
            letras.append(l[0])
# el juego se termina sin resolver:
    # se han dicho todas las letras
        if muestre_ahorcado(letras, palabra_elegida) == palabra_elegida:
            Sigue = False
            print('HAS ACERTADO ESCRIBIENDO LETRAS! La palabra era: ', palabra_elegida)
    # no quedan vidas
        if numnivel-cont == 1 and Sigue:
            dibujo(10)
            print('BOOOOOOOOM!!!!!!')
            print('HAS PERDIDO POR LÍMITE DE TIEMPO. La palabra era: ', palabra_elegida)
            Sigue = False
    # actualizar vidas
        cont += 1
    irte=input('¿quieres volver a jugar al ahorcado?')
    volver_a_jugar(irte)