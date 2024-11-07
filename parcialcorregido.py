#primero se valida
def validar_opciones(opcion: int):
    #valida que la opcion este entre el 1 y el 9
     
    while opcion < 1 or opcion > 9:
        opcion= int (input("error, debe seleccionar una opcion del 1 al 9: "))
    return opcion

def validar_edad(edad:int):
    #valida que se ingrese una edad entre 1 y 100 (coherente)

    while edad < 1 or edad > 100:
        edad = int(input("ingrese su edad (entre 1 y 100)"))
    return edad

def validar_dias_internacion(dias: int):
    #valida que los dias no sean negativos ni 0

    while dias < 1:
        dias = int(input("error, ingrese dias (entre 1 o mas) "))
    return dias


def mostrar_opciones():
    #muestra el menu de opciones
    print (
        """
        1. Cargar pacientes
        2. Mostrar la lista de pacientes
        3. Busqueda de pacientes
        4. Ordenamiento de pacientes
        5. Determinar el paciente con más dias de internación
        6. Determinar el paciente con menos dias de internación
        7. Cantidad de pacientes con días de internación mayor a 5 días
        8. Promedio de días de internación de todos los pacientes
        9. Salir
        """    )

def cargar_pacientes (lista_pacientes :list) -> list[list]:
    #carga a los nuevos con los datos ingresados por el usuario
    #retorna la lista de pacientes actualizados con los datos nuevos

    num_de_historia_clinica = int(input("ingrese el nro de historia clinica: "))
    nombre_paciente = str(input("ingrese el nombre: ")).capitalize() #mayusculas
    edad_paciente = validar_edad (int(input("ingrese la edad del paciente: ")))
    diagnostico = str(input("ingrese el diagnostico del paciente: ")).capitalize()
    cantidad_dias_internacion = validar_dias_internacion(int(input("ingrese la cantidad de dias de internacion: ")))

    datos_nuevo_paciente = [num_de_historia_clinica, nombre_paciente, edad_paciente, diagnostico, cantidad_dias_internacion]

    lista_pacientes.append(datos_nuevo_paciente)

    return lista_pacientes

def mostrar_lista_de_pacientes(lista_pacientes: list) -> None:

    #muestra todos los datos almacenados
    #lista_pacientes(list) almacenador a mostrar
    #return:
    #  (None): imprime por pantalla la lista almacenadas.

    if not lista_pacientes:
        print("no hay agregados.")
        return

    print(lista_pacientes)
    return

def buscar_paciente(lista_pacientes: list) -> None:

    #buscar por nro historial y muestra los datos.
    # ...(list) en donde busca
    #return
    #(list): muestra los datos
    #(none): imprime no encontrado

    if not lista_pacientes:
        print("no hay registrados.")
        return

    nro_clinica_a_buscar = int(input("ingrese el nro :"))

    for i in range(len(lista_pacientes)):
        if lista_pacientes[i][0] == nro_clinica_a_buscar:
            print(lista_pacientes[i])
            return

    print("no encontrado")
    return

def ord_burbuja (array: list):
    #ordena una lista usando el algoritmo de burbuja
    #array(list): la lista a ordenar

    longitud = len(array)

    for i in range(longitud):
        for j in range(longitud - 1 - i): 
            #Ponemos el -1 para dejar el último número fijo
            # (ya que el ordenamiento burbuja es así). 
            # La i hace que el algoritmo no de vueltas de más al pedo.
            if array[j][0] > array [j+1][0]: 
                # # compara [j][0] el siguiente elemento de de la lista 
                # que sigue [j+1][0]
                # Intercambio los elementos
                temporal = array [j+1]
                 #guarda el número sig al actual, para no pisarlo
                array[j+1] = array [j]
                # # A la posición del núm sig, le guardo la posición j
                array[j] = temporal 
                #A la posición j, le dejo el núm que estaba en j+1 
                # (que para no pisarlo lo guarde en temporal)


                # for i in range(len(lista_pacientes)):

                # Aquí i es un índice que se usa para recorrer la lista 
                # de pacientes. range(len(lista_pacientes)) genera una 
                # secuencia de números desde 0 hasta el tamaño de la lista 
                # menos uno. Así, i tomará todos los valores posibles de índice para acceder a
                #  cada elemento de lista_pacientes.
                # for j in range (longitud - 1 - i):

                #En este caso, j es otro índice utilizado dentro de un bucle 
                # anidado para implementar el algoritmo de ordenamiento burbuja.
                #  Este bucle recorre la lista hasta el penúltimo elemento no ordenado 
                # (de ahí longitud - 1 - i). A medida que se van haciendo pasadas 
                # (cada iteración del bucle externo controlada por i), los elementos
                #  más grandes se "burbujearán" al final de la lista, por lo que ya no
                #  es necesario comparar los últimos elementos que ya están en su lugar.
                #j + 1:

                #Este se usa para comparar el elemento actual array[j] con el siguiente 
                # elemento array[j + 1]. Si el elemento actual es mayor que el siguiente,
                #  se intercambian para ponerlos en el orden correcto.
                
def ordenamiento_de_pacientes(lista_pacientes: list) -> None:
    #ordena por numero
    if not lista_pacientes:
        return print("no hay registrados. ")
    #ordena por burbuja
    ord_burbuja(lista_pacientes)
    print(lista_pacientes)
    return

def determinar_paciente_con_mayor_dias_de_internacion(lista_pacientes: list) -> None:

    if not lista_pacientes:
        print("no hay registrados")
        return

    paciente_mayor_internacion = lista_pacientes[0]
    for i in range(1, len(lista_pacientes)):
        if lista_pacientes[i][4] > paciente_mayor_internacion[4]:
            paciente_mayor_internacion = lista_pacientes[i]

    print(paciente_mayor_internacion)
    return

def determinar_paciente_con_menor_dias_de_internacion(lista_pacientes: list) -> None: 
    if not lista_pacientes:
        print("no hay registrados")
        return

    paciente_menor_internacion = lista_pacientes[0]
    for i in range (1, len(lista_pacientes)):
        if lista_pacientes[i][4] < paciente_menor_internacion[4]:
            paciente_menor_internacion = lista_pacientes[i]

    print(paciente_menor_internacion)
    return

def determinar_pacientes_internacion_mas_5_dias(lista_pacientes: list) -> int:
    contador = 0
    for i in range(len(lista_pacientes)):
        if lista_pacientes[i][4] > 5:
            contador += 1
    return contador

def calcular_promedio_dias_internacion(lista_pacientes: list) -> float|None:
    total_dias = total_dias_de_intenacion_pacientes(lista_pacientes)
    cantidad_pacientes = len(lista_pacientes)

    if cantidad_pacientes > 0:
        return total_dias / cantidad_pacientes
    else:
        print ("no hay registrado. ")
        return

def total_dias_de_intenacion_pacientes(lista_pacientes: list) -> int: 
    acumulador = 0
    for i in range(len(lista_pacientes)):
        acumulador += lista_pacientes[i][4]
    return acumulador



def menu():
    #iterativo para el usuario
    pacientes = []
    print ("bienvenido! elija una opcion: ")
    mostrar_opciones()

    opcion = validar_opciones(int(input("elija una opcion [1-9]: ")))

    while opcion != 9:

        if opcion == 1: 
            cargar_pacientes(pacientes)

        elif opcion == 2:
            mostrar_lista_de_pacientes(pacientes)
        elif opcion == 3:
            buscar_paciente(pacientes)
        elif opcion == 4:
            ordenamiento_de_pacientes(pacientes)
        elif opcion == 5:
            determinar_paciente_con_mayor_dias_de_internacion(pacientes)
        elif opcion == 6:
            determinar_paciente_con_menor_dias_de_internacion(pacientes)
        elif opcion == 7:
            resultado = determinar_pacientes_internacion_mas_5_dias(pacientes)
            print(f"cantidad q llevan: ")

        elif opcion == 8:
            promedio = calcular_promedio_dias_internacion(pacientes)
            if promedio != None:
                print(f"promedio de dias: {promedio:.2f}")

        print("que desea hacer ahora? ")
        mostrar_opciones()
        opcion = validar_opciones(int(input("elija la opcion (1-9): ")))

    print("saliendo del sistema. ")

menu()