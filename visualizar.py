from ctypes import sizeof
import os
from xml.etree.ElementTree import ProcessingInstruction
from pysnmp.hlapi import *

# Consulta snmpget que solo devuelve el valor
def consultaSoloValor(comunidad,host,oid):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(comunidad),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid))))

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            num = [x.prettyPrint() for x in varBind]
            return num[1]

# Revisar si el archivo de texto está vacío
def revisarTextFile():
    tamanioArchivo = os.path.getsize("agentes.txt")
    if tamanioArchivo == 0:
        return False
    else:
        return True

# Funcion para tomar las direcciones IP del archivo de texto
def tomarIPAgentes():
    listaIP = []
    with open('agentes.txt','r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            listaIP.append(linea.split()[0]) 
    return listaIP

# Funcion para tomar las comunidades del archivo de texto
def tomarComunidadAgentes():
    listaComunidades = []
    with open('agentes.txt','r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            listaComunidades.append(linea.split()[2]) 
    return listaComunidades

# 1. El numero de dispostivos que estan en monitoreo
def numeroDispositivos():
    countadorDispostivos = len(open('agentes.txt').readlines())
    return countadorDispostivos

# 2. Estado de conectividad con cada agente (up or down)
def estadoConectividad(ipAgente):
    print("\n\t--- ESTADO DEL AGENTE " + ipAgente + " ---\t\n")
    HOST_UP  = True if os.system("ping -c 1 " + ipAgente) == 0 else False
    if HOST_UP:
        print("\n\t--- EL AGENTE " + ipAgente + " ESTÁ CONECTADO ---\n")
        return HOST_UP
    else: 
        print("\t--- EL AGENTE " + ipAgente + " ESTÁ DESCONECTADO ---\n\n")
        return HOST_UP

# 3. El número de interfaces de red de cada agente
def numeroInterfaces(ipAgente):
    with open('agentes.txt','r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if(linea.split()[0] == ipAgente):
                comunidadAgente = linea.split()[2]
        
    numInterfaces = consultaSoloValor(comunidadAgente,ipAgente,"1.3.6.1.2.1.2.1.0")
    return comunidadAgente,numInterfaces

# 4. Estado administrativo y descripcion de cada una de las interfaces
def estadoInterfaces(numeroInterfaces,ipAgente,comunidadAgente):
    for i in range(1,int(numeroInterfaces)+1):
        ifDescr = consultaSoloValor(comunidadAgente,ipAgente,"1.3.6.1.2.1.2.2.1.2." + str(i))
        ifAdminStatus = consultaSoloValor(comunidadAgente,ipAgente,"1.3.6.1.2.1.2.2.1.7." + str(i))

        if ifDescr[:2] == '0x':
            ifDescr = ifDescr[2:]
            ifDescr = bytes.fromhex(ifDescr)
            ifDescr = ifDescr.decode("ASCII")

        if ifAdminStatus == "1":
            print("Interfaz --> " + ifDescr + " // ESTADO: UP")
        elif ifAdminStatus == "2":
            print("Interfaz --> " + ifDescr + " // ESTADO: DOWN")
        else:
            print("Interfaz --> " + ifDescr + " // ESTADO: TESTING")

# Funcion para visualizar información general de agentes e interfaces
def visualizarAgentes():
    if revisarTextFile():
        os.system('clear')
        print("INFORMACIÓN DE AGENTES")
        
        print("\n1. Dispositivos en monitoreo: " + str(numeroDispositivos()) + "\n")
        for i in tomarIPAgentes():
            print("\t--- "+i+" ---")

        ipAgenteElegido = input("\n¿De cual agente desea saber su información?: ")
        
        print("\n2. Conectividad del agente " + ipAgenteElegido)
        agenteUPorDOWN = estadoConectividad(ipAgenteElegido)
        if agenteUPorDOWN:
            comunidadAgente,numInterfaces = numeroInterfaces(ipAgenteElegido)
            print("3. Número de interfaces del agente " + ipAgenteElegido + ":",numInterfaces)

            print("\n4. Estado administrativo y descripción de interfaces\n")
            estadoInterfaces(numInterfaces,ipAgenteElegido,comunidadAgente)

        input("\nENTER para continuar")

    else:
        os.system('clear')
        input("No hay agentes registrados")