
def visualizar_inventario(inventario): # opcion 2 - lista
    if len(inventario) == 0:
        print("\n*************************************")
        print("El inventario está vacío")
        print("*************************************")
    
    else:

        print("\n*************************************")
        print("Visualización de Inventario completo:")
        print("_______________________________________")

        for i in range(len(inventario)) :
            print(f"Herramienta: {inventario[i]["herramienta"]}, Cantidad: {inventario[i]["cantidad"]}")
        print("*************************************")


def reporte_agotados(inventario): # opcion 4  - lista
    if len(inventario) == 0:
        print("\n*************************************")
        print("El inventario está vacío")
        print("*************************************")
    else:
        print("\n*************************************")
        print("Visualización de Elementos Agotados :")
        print("_______________________________________")
        contador_agotados = 0

        for i in range(len(inventario)) :
            if inventario[i]["cantidad"] == 0: 
                print(f"Herramienta: {inventario[i]["herramienta"]}, Cantidad: {inventario[i]["cantidad"]}")
                contador_agotados += 1
        
        if contador_agotados == 0:
            print("\n*************************************")
            print("No hay elementos agotados actualmente")
            print("*************************************")
