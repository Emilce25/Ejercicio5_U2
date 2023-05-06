from clasePlandeAhorro import PlanAhorro 
import csv

def leer_datos_archivo():
    lista_planes = []
    with open("planes.csv", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")
            plan = PlanAhorro(datos[0], datos[1], datos[2], float(datos[3]), int(datos[4]), int(datos[5]))
            lista_planes.append(plan)
    return lista_planes


def actualizar_valor_vehiculo(lista_planes):
    codigo = input("Ingrese el código del plan: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    version = input("Ingrese la versión del vehículo: ")
    valor = float(input("Ingrese el valor actualizado del vehículo: "))
    for plan in lista_planes:
        if plan.codigo == codigo and plan.modelo == modelo and plan.version == version:
            plan.actualizar_valor(valor)
            print("Valor del vehículo actualizado exitosamente.")
            return
    print("No se encontró un plan con los datos ingresados.")


def mostrar_planes_valor_cuota_inferior(lista_planes):
    valor = float(input("Ingrese el valor límite de la cuota: "))
    print("Planes con valor de cuota inferior a", valor)
    for plan in lista_planes:
        valor_cuota = plan.calcular_valor_cuota()
        if valor_cuota < valor:
            print(plan.codigo, plan.modelo, plan.version)


def mostrar_monto_licitacion(lista_planes):
    codigo = input("Ingrese el código del plan: ")
    for plan in lista_planes:
        if plan.codigo == codigo:
            monto_licitacion = plan.calcular_monto_licitacion()
            print("Monto para licitar el vehículo:", monto_licitacion, "pesos.")
            return
    print("No se encontró un plan con el código ingresado.")


def modificar_cant_cuotas_licitacion(lista_planes):
    codigo = input("Ingrese el código del plan: ")
    cant_cuotas_licitacion = int(input("Ingrese la nueva cantidad de cuotas para licitar: "))
    for plan in lista_planes:
        if plan.codigo == codigo:
            plan.cant_cuotas_licitacion = cant_cuotas_licitacion
            print("Cantidad de cuotas para licitar actualizada exitosamente.")
            return
    print("No se encontró un plan con el código ingresado.")


if __name__ == '__main__':
    def mostrar_menu():
     print("1. Actualizar valor del vehículo")
     print("2. Mostrar planes con valor de cuota inferior a un valor dado")
     print("3. Mostrar monto para licitar el vehículo")
     print("4. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print("Valor del vehiculo actualizado:",actualizar_valor_vehiculo(lista_planes=[]) )
    elif opcion == "2":
        print("Planes con valor de cuota inferior:",mostrar_planes_valor_cuota_inferior (lista_planes=[]))
    elif opcion == "3":
        print("Monto para licitar el vehiculo:",mostrar_monto_licitacion (lista_planes=[]))
    elif opcion == "4":
        print("Saliendo del programa...")
    else:
        print("Opción inválida, intente de nuevo")
     