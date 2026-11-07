import time
from biblioteca.interfaz import menu as menu
from biblioteca.operaciones import carga as carga
from biblioteca.operaciones import consulta as consulta
from biblioteca.utilidades import busqueda as busqueda

print("\n*************************************")
print("Bienvenido al sistema de Inventario")
print("*************************************")

def main(): 
    inventario = [] 
    while True:
        try:
            opcion = menu.menu()

            if opcion == 7:
                break
            if opcion == 1:
                carga.carga_herramienta_existente(inventario) # ok
            if opcion == 2:
                consulta.visualizar_inventario(inventario) #ok
            if opcion == 3:
                busqueda.consultar_stock_con_clave(inventario) # ok
            if opcion == 4:
                consulta.reporte_agotados(inventario) #ok
            if opcion == 5:
                inventario.append(carga.alta_nuevo_producto(inventario))
            if opcion == 6:
                busqueda.actualizar_stock_con_clave(inventario) 
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
        

        

main()

print("Ud ha salido del sistema de inventario")


time.sleep(6)