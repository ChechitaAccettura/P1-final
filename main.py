from biblioteca.interfaz import menu as menu
from biblioteca.operaciones import carga as carga
from biblioteca.operaciones import consulta as consulta
from biblioteca.utilidades import busqueda as busqueda
from biblioteca.utilidades import validaciones as validaciones


print("Bienvenido al sistema de Inventario")

def main(): #CORRECTA CREO
    inventario = []
    opcion = menu.menu()
    while opcion != 7:
        if opcion == 1:
            carga.carga_herramienta_existente()
        if opcion == 2:
            consulta.visualizar_inventario()
        if opcion == 3:
            busqueda.consultar_stock_con_clave()
        if opcion == 4:
            consulta.reporte_agotados
        if opcion == 5:
            carga.alta_nuevo_producto()
        if opcion == 6:
            busqueda.actualizar_stock_con_clave

        

main()

print("Ud ha salido del sistema de inventario")
