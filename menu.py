from datetime import datetime
import os
import time
from visualizar import visualizarAgentes
from agregar import agregarAgente
from eliminar import eliminarAgente
from reporte import generarReporte

def menu():
    os.system('clear')
    print("PRÁCTICA 1: Adquisición de información usando SNMP")
    print("ALUMNO: Humberto Vázquez Santiago")
    print("\n\t\tMENÚ\n")
    print("1. Visualizar información de agentes")
    print("2. Agregar agente")
    print("3. Eliminar agente")
    print("4. Generar reporte")
    print("5. Salir")

    opcionMenu = input("\nEliga una opcion: ")
    if opcionMenu == "1":
        visualizarAgentes()
        menu()
    elif opcionMenu == "2":
        agregarAgente()
        menu()
    elif opcionMenu == "3":
        eliminarAgente()
        menu()
    elif opcionMenu == "4":
        generarReporte()
        menu()
    elif opcionMenu == "5":
        os.system('clear')
        exit
    else:
        input("No has pulsado una opción correcta")
        menu()