def IntInputValid(message): # Función para que el user ponga un input numérico valido.
    userInput = input(f'{message}\n> ')
    while userInput.isalpha() or int(userInput) < 0: # Loop para que se vuelva a preguntar hasta tener una cantidad correcta.
        print("Valor incorrecto, ingresa nuevamente la cantidad.")
        userInput = input(f'{message}\n> ')
    userInput = int(userInput)
    return userInput

def CargaDeAnimales(animal_number): # Función para añadir el dict 'animal' en la lista 'animals'.
    for i in range(1, animal_number + 1):
        print("")
        print(f"ANIMAL {i}:")
        animal = {'Especie': '', 'Población': 0, 'Ubicación': ''}
        animal['Especie'] = input('¿Cuál es la especie del animal?\n> ').capitalize()
        animal['Población'] = IntInputValid('¿Cuánto es la población del animal?')
        if animal['Población'] >= 10000:
            print("Fuera de peligro de extincion.")
        elif animal['Población'] == 0:
            print('Extinto.')
        else:
            print("En vias de extincion.")
        animal['Ubicación'] = input('¿Cuál es el habitad/ubicación del animal?\n> ').capitalize()
        animals.append(animal)
    return print(animals)
 
def PrintAnimals(listWithDict): # Función que imprime cada key y value de los diccionarios dentro de la lista 'animals'.
    if len(listWithDict) == 0:
        print('La lista esta vacia.')
    else:
        for i in range(len(listWithDict)):
            print(f'Animal {i + 1}')
            for x in animals[i].items():
                print(f'   {x[0]}: {x[1]}')

def WelcomePrint(): # Función que imprime un saludo de bienvenida.
    print("#"*41)
    print("#"*14 + " "*13 + "#"*14)
    print("#"*10 + "     Bienvenido a    " + "#"*10)
    print("#"*7 + "      Animal Register     " + "#"*8)
    print("#"*10 + "     Aplication     " + "#"*11)
    print("#"*14 + " "*12 + "#"*15)
    print("#"*41)

def FarewellPrint():
    print("#"*41)
    print("#"*14 + " "*13 + "#"*14)
    print("#"*10 + "    Thanks for use   " + "#"*10)
    print("#"*7 + "      Animal Register     " + "#"*8)
    print("#"*10 + "     Aplication     " + "#"*11)
    print("#"*14 + " "*12 + "#"*15)
    print("#"*41)

def MenuApp(): # Función que imprime opciones del menu y optiene la eleccion.
    option = ""
    while option != 3:
        print("="*41)
        print("Menu:")
        print("1). Ingresar nuevo registro de animales.")
        print("2). Ver registro de animales cargados.")
        print("3). Salir del programa.")
        print("="*41)
        option = input('Elige una opcion:\n> ')
        while option.isalpha() or int(option) < 0 or int(option) > 3: # Loop para que se vuelva a preguntar hasta tener una cantidad correcta.
            print("Opción no valida, elige nuevamente.")
            option = input('> ')
        option = int(option)
        if option == 1:
            animal_number = IntInputValid('¿Cuántos animales deseas registrar?') # Almacenamos el input correcto.
            CargaDeAnimales(animal_number) # Ejecutamos la funcion con la variable del input como argumento.
        elif option == 2:
            PrintAnimals(animals) # Ejecutamos la funcion para imprimir la lista.
    FarewellPrint()


# Inicio del programa:

# Variables para almacenar los datos:
animals = []
animal_number = ''

# Llamamos a las funciones para correr el programa:
WelcomePrint()
MenuApp()
