

def menu(): # lista
    while True:   
        print(" \n 1 : Cargar herramientas existentes \n 2 : Visualización de inventario \n 3 : Consulta de stock \n 4 : Reporte de agotados \n 5 : Alta de nuevo producto \n 6 : Actualización de stock (venta / ingreso) \n 7 : Salir \n_______________________________________")
        try:
            opcion = (input("Ingrese la opción Deseada: ")).strip()
            if opcion == "":
                raise KeyError("La entrada no puede estar vacía")
            opcion = int(opcion)
            if opcion <= 7 and opcion >= 1:
                return opcion
            else:
                raise KeyError("La opción ingresada debe ser un número válido entre 1 y 7")
        except ValueError:
            print("Debe ingresar una entrada numérica del 1 al 7")
        except KeyError as e:
            print(e)
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
        
         