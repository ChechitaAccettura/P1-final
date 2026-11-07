

def carga_herramienta_existente(inventario): #opcion 1
        try:
            cantidad_cargas = input("Ingrese la cantidad de herramientas que va a cargar: ")
            if cantidad_cargas == "":
                raise ValueError("\nLa entrada no puede estar vacía")
            else:
                cantidad_cargas = int(cantidad_cargas)
                if cantidad_cargas <= 0:
                    raise KeyError("El número de herramientas que desea cargar debe ser un número mayor que 0")
                 
                for i in range(cantidad_cargas):  
                    clave = input(f"\nIngrese el producto {i+1}° que desea actualizar: ").strip().capitalize()
                    if clave == "":
                        print("\nEl nombre del producto no puede estar vacía")
                    else:
                        herramienta_encontrada = None
                        for herramienta in inventario:
                            if herramienta["herramienta"] == clave:
                                herramienta_encontrada = herramienta
                                break

                        if herramienta_encontrada is not None:
                            print(f"La herramienta {clave} ya se encuentra en el inventario. ")
                            while True:
                                try:
                                    cantidad = int(input(f"\nIngrese el stock nuevo de {clave}: "))
                                    if cantidad >= 0:
                                        herramienta_encontrada["cantidad"] = cantidad  
                                        print(f"\nEl stock de {clave} ha sido actualizado con éxito, quedan en total {herramienta_encontrada["cantidad"]}")
                                        break
                                        
                                    else:
                                        raise KeyError("El stock debe ser un número positivo")
                                except ValueError:
                                    print("El stock nuevo debe ser mayor o igual a 0")
                                except KeyError as e:
                                    print(e)
                    
                        else:
                            print(f"La herramienta {clave} no se encuentra en el inventario. ")
                            while True:
                                try:
                                    cantidad = int(input(f"\nIngrese el stock de {clave}: "))
                                    if cantidad >= 0:
                                        inventario.append({"herramienta": clave, "cantidad": cantidad}) 
                                        print(f"\nEl producto {clave} ha sido agregado con éxito. Su stock actual es {cantidad}")
                                        break
                                    else:
                                        raise KeyError("El stock debe ser un número positivo")
                                except ValueError:
                                    print("El stock nuevo debe ser mayor o igual a 0")
                                except KeyError as e:
                                    print(e)
                                        
                print("\nCarga de herramientas finalizada.")
        except ValueError:
            print("Debe ingresar la cantidad de cargas en números enteros.")
        except KeyError as e:
            print(e)
        except Exception as e:
            print(f"\nHa ocurrido un error inesperado {e}")







def alta_nuevo_producto(inventario): # opcion 5 
    try:
        clave = input("Ingrese el elemento que desea agregar al inventario: ").strip().capitalize()
        if clave == "":
            raise ValueError("El nombre del producto no puede estar vací0.")
        elif clave in [herramienta["herramienta"] for herramienta in inventario] or clave.isdigit():
            
            raise ValueError("Debe ingresar una herramienta NUEVA en formato texto.")   
        else:
            try:
                cantidad = int(input(f"Ingrese la cantidad de elementos que desea agregar a {clave}: "))
                if cantidad >= 0:
                    inventario.append({"herramienta": clave, "cantidad": cantidad})  
                    print("El registro ha sido ingresado con éxito")
            except ValueError:
                print(f"Debe ingresar la cantidad de {clave}(s) en números enteros")

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Ha ocurrido un error inesperado {e}")