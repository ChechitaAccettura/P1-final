inventario = [{"Herramienta": "Algo", "Cantidad": 23}] #sacar despues



def consultar_stock_con_clave():
    pass

def actualizar_stock_con_clave():
    pass

def busqueda(inventario):
        buscada = input("Ingrese el elemento que desea buscar: ").strip().capitalize()
        for herramientas in inventario:
            if herramientas["Herramienta"] == buscada:
                return buscada

print(busqueda(inventario))