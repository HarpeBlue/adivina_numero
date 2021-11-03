import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un número entre 1 y 100: '))
    while numero_aleatorio != numero_elegido:
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mayor')
        else:
            print('Busca un numero menor')
        numero_elegido = int(input('Elige otro número: '))

    print('¡Has elegido el número correcto!')



if __name__ == '__main__':
    run()
