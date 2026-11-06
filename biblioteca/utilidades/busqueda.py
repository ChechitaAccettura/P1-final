
def consultar_stock_con_clave(inventario): # opcion 3 - lista
    if len(inventario) == 0:
        print("\n*************************************")
        print("El inventario está vacío")
        print("*************************************")

    else:
        try:
            clave = input("Ingrese el elemento por el que desea consultar: ").strip().capitalize()
            if clave == "":
                raise ValueError("La entrada no puede estar vacía")
            elif clave not in [herramienta["herramienta"] for herramienta in inventario]:
                raise KeyError(f"\nLa herramienta {clave} no está en el inventario")
            else:
                for i in range(len(inventario)) :
                    if inventario[i]["herramienta"] == clave: 
                        print("\n *************************************")
                        print(f"Herramienta: {inventario[i]["herramienta"]}, Cantidad: {inventario[i]["cantidad"]}")  
                        print("\n *************************************\n")

        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)

    
def actualizar_stock_con_clave(inventario): #opcion 6 - lista
    if len(inventario) == 0:
        print("\n*************************************")
        print("El inventario está vacío")
        print("*************************************")

    else:
        try:
            clave = input("Ingrese el elemento que desea actualizar (INGRESO/VENTA): ").strip().capitalize()
            if clave == "":
                raise ValueError("La entrada no puede estar vacía")
            if clave not in [herramienta["herramienta"] for herramienta in inventario]:
                raise KeyError("Debe ingresar una herramienta existente.")
            for i in range(len(inventario)) :
                if inventario[i]["herramienta"] == clave: 
                    try:
                        opcion = int(input(f"Ingrese 1 para agregar items al producto {clave} y 2 para ingresar una venta:  "))
                        if opcion == 1:
                            try:
                                agregar = int(input(f"Ingrese la cantidad de elementos que desea agregar a {clave}: "))
                                if agregar < 0:
                                    print("Debe ingresar un número entero positivo para la cantidad a agregar")
                                else:
                                    inventario[i]["cantidad"] += agregar
                                    print(f"El stock de {clave} fue correctamente actualizado. Actualmente quedan {inventario[i]["cantidad"]} unidades")
                            except ValueError:
                                print("Debe ingresar un número entero para la cantidad a agregar")
                        elif opcion == 2:
                            try:
                                vender = int(input(f"Ingrese la cantidad de elementos que desea vender de {clave}: "))
                                if (inventario[i]["cantidad"] - vender) < 0:
                                    raise ValueError("No puede realizar esta venta puesto que no dispone de stock suficiente. ")
                                else:
                                    inventario[i]["cantidad"] -= vender
                                    print(f"El stock de {clave} fue correctamente actualizado. Actualmente quedan {inventario[i]["cantidad"]} unidades")

                            except ValueError:
                                print("Debe ingresar un número entero para la cantidad a agregar")
                        else:
                            raise KeyError("Debe ingresar 1 o 2 para la opción de actualización de stock")
                    except Exception as e:
                        print(f"Ha ocurrido un error inesperado {e}")

        except ValueError as e:
            print(e)
