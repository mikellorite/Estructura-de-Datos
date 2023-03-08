import funciones
import time
print('BIENVENID@')
print('1: JUGAR AL AHORCADO')
print('2: CAMBIAR LA LISTA DE PALABRAS DEL AHORCADO')
print('3: SALIR')
decision1 = input('¿Qué quieres hacer?: ')
funciones.limpiar_pantalla()

while decision1!='3':
    if decision1=='1':
        time.sleep(0.5)
        funciones.ahorcado()
    elif decision1=='2':
        time.sleep(0.5)
        funciones.menu_cambiar_lista()
    else:
        print('Tas equivocao')
        funciones.limpiar_pantalla()
        time.sleep(0.5)
    print('BIENVENID@')
    print('1: JUGAR AL AHORCADO')
    print('2: CAMBIAR LA LISTA DE PALABRAS DEL AHORCADO')
    print('3: SALIR')
    decision1 = input('¿Qué quieres hacer?: ')
