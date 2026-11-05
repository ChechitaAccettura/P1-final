
def visualizar_inventario(inventario): # opcion 2 

    print("\n *************************************")
    print("Visualización de Inventario completo:")
    print("_______________________________________")

    for i in range(len(inventario)) :
        print(f"Herramienta: {inventario[i]["herramienta"]}, Cantidad: {inventario[i]["cantidad"]}")
    print("***************************")


def reporte_agotados(inventario): # opcion 4 
    print("\n*************************************")
    print("Visualización de Elementos Agotados :")
    print("_______________________________________")

    for i in range(len(inventario)) :
        if inventario[i]["cantidad"] == 0: 
            print(f"Herramienta: {inventario[i]["herramienta"]}, Cantidad: {inventario[i]["cantidad"]}")
    print("***************************")