from ..utilidades import busqueda as busqueda

def carga_herramienta_existente(inventario): #opcion 1
    while True:
        try:
            cantidad_cargas = input("Ingrese la cantidad de herramientas que va a cargar: ")
            if cantidad_cargas == "":
                raise ValueError("\nLa entrada no puede estar vacía")
            else:
                cantidad_cargas = int(cantidad_cargas)
                for i in range(cantidad_cargas +1):

                    clave = input(f"\nIngrese el elemento {i+1} que desea actualizar: ").strip().capitalize()
                    if clave == "":
                        raise ValueError("\nLa entrada no puede estar vacía")
                    elif clave not in [herramienta["herramienta"] for herramienta in inventario]:
                        raise KeyError("\nDebe ingresar una herramienta que esté en el inventario")    
                    else:
                        for i in range(len(inventario)) :
                            if inventario[i]["herramienta"] == clave: 
                                cantidad = int(input(f"\nIngrese la cantidad de elementos que desea agregar a {clave}: "))
                                if cantidad > 0:
                                    inventario[i]["cantidad"] += cantidad  
                                    print(f"\nEl stock de {clave} ha sido actualizaco con éxito, quedan en total {inventario[i]["cantidad"]}")
                                print("\n *************************************\n")

        except ValueError as e:
            print(e)
        except KeyError as e:
            print(e)
        except Exception as e:
            print(f"\nHa ocurrido un error inesperado {e}")







def alta_nuevo_producto(inventario): # opcion 5 - lista
    try:
        clave = input("\nIngrese el elemento que desea agregar al inventario: ").strip().capitalize()
        if clave == "":
            raise ValueError("\nLa entrada no puede estar vacía")
        elif clave in [herramienta["herramienta"] for herramienta in inventario] or clave.isdigit():
            
            raise KeyError("\nDebe ingresar una herramienta NUEVA")    
        else:
            try:
                cantidad = int(input(f"\nIngrese la cantidad de elementos que desea agregar a {clave}: "))
                if cantidad >= 0:
                    nuevo_producto = ({"herramienta": clave, "cantidad": cantidad})  
                    print("\nEl registro ha sido ingresado con éxito")
                    return nuevo_producto
                    
                else:
                    raise ValueError("La cantidad debe ser mayor o igual a 0")
            except ValueError:
                print(f"\nDebe ingresar la cantidad de {clave} en números enteros")

    except ValueError as e:
        print(e)
    except KeyError as e:
        print(e)
    except Exception as e:
        print(f"\nHa ocurrido un error inesperado {e}")