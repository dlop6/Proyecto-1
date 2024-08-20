from Conjunto import Conjunto


conjuntos = []
u = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
universo = Conjunto(len(u), "U")
for value in u:
    universo.add(value)

conjuntos.append(universo)

while True:
    

    print("Bienvenido al programa de conjuntos.\n1. Crear un conjunto.\n2. Ver todos los conjuntos disponibles.\n3. Operaciones entre conjuntos.\n4. Salir.")
    


    opcion = input("Ingrese la opción que desea realizar: ")

    if opcion == "1":
        print("Creando un conjunto.")
        try:
            size = int(input("Ingrese el tamaño del conjunto: "))
            name = input("Ingrese el nombre del conjunto: ")
            conjunto = Conjunto(size, name)
            print("Solo puede ingresar elementos del alfabeto en español y números del 0 al 9.")
            
            for i in range(size):
                elemento = input(f"\nIngrese el elemento {i + 1}: ")
                if elemento.isalnum():  
                    conjunto.add(elemento.lower())
                else:
                    print("Elemento inválido.")
            
            print("Conjunto creado.")
            conjuntos.append(conjunto)
        except ValueError:
            print("Error: Tamaño del conjunto debe ser un número entero.")
        
    elif opcion == "2":
        print("Conjuntos disponibles:")
        for i, conjunto in enumerate(conjuntos):
            print(f"Conjunto {i + 1}: {conjunto.name}")
            print(f"Elementos: {conjunto.__str__()}")
    
    elif opcion == "3":
        print("Operaciones entre conjuntos.\n1. Unión.\n2. Intersección.\n3. Diferencia.\n4. Diferencia Simétrica.\n5. Complemento")
        operacion = input("Ingrese la operación que desea realizar: ")
        
        if operacion in ["1", "2", "3", "4"]:
            conjunto1_name = input("Ingrese el nombre del primer conjunto: ")
            conjunto2_name = input("Ingrese el nombre del segundo conjunto: ")

            conjunto1 = next((c for c in conjuntos if c.name == conjunto1_name), None)
            conjunto2 = next((c for c in conjuntos if c.name == conjunto2_name), None)

            if not conjunto1 or not conjunto2:
                print("Uno o ambos conjuntos no fueron encontrados.")
                continue

            if operacion == "1":
                union = conjunto1.union(conjunto2)
                print(f"Unión de {conjunto1.name} y {conjunto2.name}: {union.__str__()}")            

            elif operacion == "2":
                interseccion = conjunto1.interseccion(conjunto2)
                print(f"Intersección de {conjunto1.name} y {conjunto2.name}: {interseccion.__str__()}")
            
            elif operacion == "3":
                diferencia = conjunto1.diferencia(conjunto2)
                print(f"Diferencia de {conjunto1.name} y {conjunto2.name}: {diferencia.__str__()}")
            
            elif operacion == "4":
                diferencia_simetrica = conjunto1.diferencia_simetrica(conjunto2)
                print(f"Diferencia Simétrica de {conjunto1.name} y {conjunto2.name}: {diferencia_simetrica.__str__()}")
            
        elif operacion == "5":
            conjunto1_name = input("Ingrese el nombre del primer conjunto: ")
            conjunto1 = next((c for c in conjuntos if c.name == conjunto1_name), None)

            if not conjunto1:
                print("Uno o ambos conjuntos no fueron encontrados.")
                continue

            complemento = conjunto1.complemento(universo)
            print(f"Complemento de {conjunto1.name} y {universo.name}: {complemento.__str__()}")
        else:
            print("Opción inválida. Inténtelo de nuevo.")
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción inválida. Inténtelo de nuevo.")
