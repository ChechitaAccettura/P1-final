
def consultar_stock_con_clave(inventario): # opcion 3
    try:
        clave = input("Ingrese el elemento por el que desea consultar: ").strip().capitalize()
        if clave not in [herramienta["herramienta"] for herramienta in inventario]:
            raise ValueError("Debe ingresar una herramienta que esté en el inventario")
        for i in range(len(inventario)) :
            if inventario[i]["herramienta"] == clave: 
                print("\n *************************************")
                print(f"Herramienta: {inventario[i]["herramienta"]}, Cantidad: {inventario[i]["cantidad"]}")  
                print("\n *************************************\n")

    except ValueError:
        print("Debe ingresar una herramienta que esté en el inventario")
    
def actualizar_stock_con_clave(inventario): #opcion 6
    try:
        clave = input("Ingrese el elemento que desea actualizar: ").strip().capitalize()
        if clave not in [herramienta["herramienta"] for herramienta in inventario]:
            raise ValueError("Debe ingresar una herramienta que esté en el inventario")
        for i in range(len(inventario)) :
            if inventario[i]["herramienta"] == clave: 
                try:
                    agregar = int(input(f"Ingrese la cantidad de elementos que desea agregar a {clave}: "))
                    if agregar < 0:
                        print("Debe ingresar un número entero positivo para la cantidad a agregar")
                    else:
                        inventario[i]["cantidad"] += agregar
                except ValueError:
                    print("Debe ingresar un número entero para la cantidad a agregar")

    except ValueError:
        print("Debe ingresar una herramienta que esté en el inventario")
