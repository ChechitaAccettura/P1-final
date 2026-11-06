from ..utilidades import busqueda as busqueda

def carga_herramienta_existente(inventario): #opcion 1
    try:
        clave = input("Ingrese el elemento que desea actualizar: ").strip().capitalize()
        if clave == "":
            raise ValueError("La entrada no puede estar vacía")
        elif clave not in [herramienta["herramienta"] for herramienta in inventario]:
            raise ValueError("Debe ingresar una herramienta que esté en el inventario")    
        else:
            for i in range(len(inventario)) :
                if inventario[i]["herramienta"] == clave: 
                    cantidad = int(input(f"Ingrese la cantidad de elementos que desea agregar a {clave}: "))
                    if cantidad > 0:
                        inventario[i]["cantidad"] += cantidad  
                        print(f"El stock de {clave} ha sido actualizaco con éxito, quedan en total {inventario[i]["cantidad"]}")
                    print("\n *************************************\n")

    except ValueError:
        print("Debe ingresar una herramienta que esté en el inventario")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado {e}")







def alta_nuevo_producto(inventario): # opcion 5 
    try:
        clave = input("Ingrese el elemento que desea agregar al inventario: ").strip().capitalize()
        if clave == "":
            raise ValueError
        elif clave in [herramienta["herramienta"] for herramienta in inventario] or clave.isdigit():
            
            raise ValueError    
        else:
            try:
                cantidad = int(input(f"Ingrese la cantidad de elementos que desea agregar a {clave} "))
                if cantidad > 0:
                    inventario.append({"herramienta": clave, "cantidad": cantidad})  
                    print("El registro ha sido ingresado con éxito")
            except ValueError:
                print(f"Debe ingresar la cantidad de {clave} en números enteros")

    except ValueError:
        print("Debe ingresar una herramienta en formato texto.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado {e}")