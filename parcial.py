continuar = "s"
contador_pacientes = 0
contador_dias = 0


pacientes =[]

# comenzamos preguntando si quiere ingresar e ignoramos mayusculas y minusculas.
continuar = input ("bienvenidos a clinica 'la fuerza': desea ingresar s/n:  ").lower()

def mostrar_menu (menu: list)->list:
    menu = print ('''
        sistema de gestion de clinica: 
        1. cargar pacientes
        2. mostrar todos los pacientes
        3. buscar pacientes por numero de historia clinica
        4. ordenar pacientes por numero de historia clinica
        5. mostrar pacientes con mas dias de internacion
        6. mostrar pacientes con menos dias de internacion
        7. cnatidad de pacientes con mas de 5 dias de internacion
        8. promedio de dias de internacion con todos los pacientes
        9. salir''')
    
# sistema de carga de pacientes, se le pregunta la cantidad de pacientes
#  que quiere ingresar   
def cargar_pacientes (pacientes):
    cantidad = int(input("ingrese la cantidad de pacientes a cargar: "))
    pacientes = []
    for i in range(cantidad):
        historia_clinica = input("ingrese el numero de historia clinica: ")
        nombre = input("ingrese el nombre: ")
        dias_inter = int(input("ingrese los dias de internacion: "))
        pacientes.append([historia_clinica, nombre, dias_inter, cantidad])
        
        print (f"se cargo el paciente con historial clinica: {historia_clinica}, nombre: {nombre}, dias de internacion: {dias_inter}")

    return pacientes

def mostrar_pacientes(pacientes: list)->list:
    if pacientes:
        for paciente in pacientes:
            historial = paciente [0]
            nombre = paciente[1]
            dias = paciente[2]
    print (f"historial clinica: {historial[0]}, nombre: {nombre[1]}, dias de internacion: {dias[2]},")



def buscar_pacientes(pacientes):
    paciente_buscado = int(input("ingrese el numero de historia clinica del paciente que desea buscar: "))
    for paciente in pacientes:
        if paciente[0] == paciente_buscado:
            historia_clinica = paciente [0]
            nombre_paciente = paciente[1]
            dias_internacion = paciente[2]
             
            print(f"se encontro: {nombre_paciente}, con numero de historia clinica: {historia_clinica}, y {dias_internacion} dias de internacion.")
        else:
            print("no se encontraron pacientes con ese nombre; vuelva a intentarlo.")
        return
    
def ordenar_pacientes(pacientes):
    if len(pacientes) == 0:
        print ("no hay pacientes.")
        return
    n = len(pacientes)

    for i in range(n):
        for j in range(0, n-i-1):
            if pacientes[j][0] > pacientes[j+1][0]:
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]

        print ("pacientes ordenados")


def pacientes_mas_dias(pacientes):
    if len (pacientes) == 0:
        print ("no hay pacientes ingresados")
        return
    
    if pacientes_mas_dias == pacientes[1]:
        for paciente in pacientes:
            if paciente[1] > pacientes_mas_dias[1]:
                pacientes_mas_dias = paciente


    print (f"el paciente con mas cantidad de dias es: {paciente[1]}")


def paciente_menos_dias(pacientes):
    if len (pacientes) == 0:
        print ("no hay pacientes")
        return
    
    paciente_menos_dias = pacientes[2]
    for paciente in pacientes:
        if paciente[2] > paciente_menos_dias[2]:
            paciente_menos_dias = paciente

    print (f"el paciente con menos dias es: {paciente[2]}")


def inter_mas_5 (pacientes: list):

    paciente_encontrado = False
    
    print ("paciente con dias de internacion mayor a 5")
    for paciente in pacientes:
        if paciente[2] > 5:
            historial = paciente[0]
            nombre = paciente[1]
            dias = paciente [2]

            print (f"nro historial clinica: {historial}, nombre: {nombre}, cantidad de dias: {dias}")
            paciente_encontrado = True

    paciente_encontrado == False and print ("no se encontraron pacientes.")



def promedio (pacientes):
     contador_pacientes ==  pacientes[1].append

     contador_dias == pacientes[2].append

     contador_pacientes/contador_dias == promedio

     print (f"el promedio de internacion de todos los pacientes es de: {contador_pacientes}/{contador_dias} = {promedio}")

#saliendo del sistema
def salir ():
    print ("Saliendo del sistema.")


#bucle principal
while continuar.lower() == "s":
    mostrar_menu (mostrar_menu)
    opcion = input("seleccione una opcion: ")
    



    match opcion :
        case "1": 
            print ("cargar pacientes")
            cargar_pacientes(pacientes)
        case "2":
            print("mostrar todos los pacientes")
            mostrar_pacientes(pacientes)
        case "3":
            print ("buscar pacientes por numero de historia clinica")
            buscar_pacientes(pacientes)
        case "4":
            print("ordenar pacientes por numero de historia clinica")
            ordenar_pacientes(pacientes)
        case "5":
            print ("mostrar pacientes con mas cantidad de dias de internacion")
            pacientes_mas_dias(pacientes)
        case "6":
            print ("mostrar pacientes con menos dias de internacion")
            paciente_menos_dias(pacientes)
        case "7":
            print ("cantidad de pacientes con mas de 5 dias de internacion") 
            inter_mas_5(pacientes)
        case "8":
            print ("promedio de dias de internacion con todos los pacientes") 
            promedio(pacientes)
        case "9":
            print ("saliendo")
            salir()
        case _ :
            print("opcion no valida intente nuevamente ") 
                                

    continuar  = input("desea continuar s/n: ")

    #ROMPE EL CODIGO

 