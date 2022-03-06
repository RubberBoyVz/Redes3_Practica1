import os
import createRRD
from visualizar import revisarTextFile, tomarIPAgentes

def eliminarAgente():
    if revisarTextFile():
        os.system('clear')
        print("ELIMINAR AGENTE\n")
        print("Selecciona un agente:\n")
        for i in tomarIPAgentes():
            print("\t--- "+i+" ---")
        direccionIP = input("\nIntroduce la direccion IP del agente que deseas eliminar: ")

        with open("agentes.txt", "r") as archivo:
            lineas = archivo.readlines()
        with open("agentes.txt", "w") as archivo:
            for linea in lineas:
                if not linea.startswith(direccionIP):
                    archivo.write(linea)

        createRRD.eliminarArchivos(direccionIP)
        input("\nAgente eliminado con exito\nENTER para continuar")
    else:
        os.system('clear')
        input("No hay agentes registrados")