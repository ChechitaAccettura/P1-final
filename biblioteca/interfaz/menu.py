

def menu():
    while True:   
        print(" \n 1 : Cargar herramientas existentes \n 2 : Visualización de inventario \n 3 : Consulta de stock \n 4 : Reporte de agotados \n 5 : Alta de nuevo producto \n 6 : Actualización de stock (venta / ingreso) \n 7 : Salir")
        try:
            opcion = int(input("Ingrese la opción Deseada: "))
            return opcion
        except ValueError:
            print("La opción ingresada debe ser un número válido")
         