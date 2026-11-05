from ..utilidades import busqueda as busqueda

inventario = [{"Herramienta": "Culo", "Cantidad": 23}] #sacar despues


def carga_herramienta_existente(): #completar
    
    buscar_herramienta = busqueda.busqueda(inventario)
    if not buscar_herramienta:
        raise ValueError("La entrada no puede estar vacía")
    elif buscar_herramienta == None:
        print("La herramienta no existe, debe cargarla desde el menú principal ")
    else:
        print(f"\n El stock del producto {buscar_herramienta} es de {inventario[buscar_herramienta]} unidades.\n")
        try:
            cantidad = int(input(f"Ingrese la cantidad actual de {buscar_herramienta} que desea agregar al stock: "))
            inventario.update()
        except ValueError:
            print("Debe ingresar una cantidad válida.")




def alta_nuevo_producto(inventario): # opcion 5 CORREGIR
    while True:
        try:

            nueva_herramienta = busqueda.busqueda(inventario)
            if not nueva_herramienta:
                raise ValueError("La entrada no puede estar vacía")
           
            if nueva_herramienta : 
                try:
                    cantidad = int(input(f"Ingrese la cantidad actual de {nueva_herramienta} disponibles: "))
                    if cantidad > 0:
                        nuevo_ingreso = {"Herramienta": nueva_herramienta, "Cantidad": cantidad}
                        inventario.append(nuevo_ingreso)
                        break

                    
                except ValueError:
                    print("Debe ingresar la cantidad en números")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado {e}")

alta_nuevo_producto(inventario)

print(inventario)
