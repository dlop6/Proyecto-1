from Conjunto import Conjunto


conjuntos = []

while True:
    print ("="*40)
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
                    conjunto.add(elemento)
                else:
                    print("Elemento inválido.")
            
            print("Conjunto creado.")
            conjuntos.append(conjunto)
        except ValueError:
            print("Error: Tamaño del conjunto debe ser un número entero.")
        
    elif opcion == "2":
        print("Conjuntos disponibles:")
        for i, conjunto in enumerate(conjuntos):
            print("-"*40)
            print(f"Conjunto : {conjunto.name}")
            print(f"Elementos: {conjunto.buckets}")
    
    elif opcion == "3":
        print("Operaciones entre conjuntos.\n1. Unión.\n2. Complemento.\n3. Intersección.\n4. Diferencia.\n5.Diferencia Simétrica")
        operacion = input("Ingrese la operación que desea realizar:\n")
        
        if operacion in ["1", "2", "3", "4", "5"]:
            conjunto1_name = input("Ingrese el nombre del primer conjunto: ")
            conjunto2_name = input("Ingrese el nombre del segundo conjunto: ")

            conjunto1 = next((c for c in conjuntos if c.name == conjunto1_name), None)
            conjunto2 = next((c for c in conjuntos if c.name == conjunto2_name), None)

            if not conjunto1 or not conjunto2:
                print("Uno o ambos conjuntos no fueron encontrados.")
                continue

            if operacion == "1":
                union = conjunto1.union(conjunto2)
                print(f"Unión de {conjunto1.name} y {conjunto2.name}: {union}")
                
            elif operacion == "2":
                complemento = conjunto1.complemento(conjunto2)
                print(f"Complemento de {conjunto1.name} y {conjunto2.name}: {complemento}")

            elif operacion == "3":
                pass
            
            elif operacion == "4":
                pass
            
            elif operacion == "5":
                pass
            
        else:
            print("Opción inválida. Inténtelo de nuevo.")
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción inválida. Inténtelo de nuevo.")
