import os
import createRRD

def agregarAgente():
    os.system('clear')
    print("AGREGAR AGENTE\n")
    direccionIP = input("Introduce la direccion IP: ")
    versionSNMP = input("Introduce la version de SNMP: ")
    comunidad = input("Introduce el nombre de la comunidad: ")
    puerto = input("Introduce el puerto: ")

    nuevoAgente = direccionIP + " " + versionSNMP + " " + comunidad + " " + puerto + "\n"

    archivo = open('agentes.txt','a')
    archivo.write(nuevoAgente)
    archivo.close()

    createRRD.crearBasesDeDatos(direccionIP)
    input("\nAgente agregado con exito\nENTER para continuar")