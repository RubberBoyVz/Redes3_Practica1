import os
from visualizar import consultaSoloValor, numeroInterfaces, tomarIPAgentes,revisarTextFile
from updateRRD import iniciarActualizacion
from graphRRD import CrearGraficas
import glob
from dominate import document
from dominate.tags import *
import pdfkit

def tomarComunidadAgente(ipAgente):
        with open('agentes.txt','r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if linea.split()[0] == ipAgente:
                    comunidadAgente = linea.split()[2] 
        return comunidadAgente

def generarReporte():
    if revisarTextFile():
        os.system('clear')
        print("GENERAR REPORTE")
        print("Selecciona un agente:\n")
        for i in tomarIPAgentes():
                print("\t--- "+i+" ---")
        ipAgente = input("\nSeleccion: ")
        comunidadAgente = tomarComunidadAgente(ipAgente)
        interfazAgente = input("Interfaz del agente: ")
        tiempoMuestreo = input("Tiempo muestreo en segundos: ")
        
        print("Espere por favor...")
        iniciarActualizacion(comunidadAgente,ipAgente,interfazAgente,tiempoMuestreo)
        CrearGraficas(ipAgente)

        infoSistemaOperativo = consultaSoloValor(comunidadAgente,ipAgente,"1.3.6.1.2.1.1.1.0")
        ubicacionGeografica = consultaSoloValor(comunidadAgente,ipAgente,"1.3.6.1.2.1.1.6.0")
        numInterfaces = numeroInterfaces(ipAgente)
        c = int(consultaSoloValor(comunidadAgente,ipAgente,"1.3.6.1.2.1.1.3.0"))
        tiempoActivo = str(int(c/100/60)) + " minutos"

        graficas = glob.glob('*'+ipAgente+'.png')

        with document(title="Reporte") as doc:
            h1("Reporte de informacion del dispositivo")
            if "Ubuntu" in infoSistemaOperativo:
                div(img(src='ubuntu.png'))
            else:
                div(img(src='windows.png'))
            p("Sistema operativo: "+infoSistemaOperativo)
            p("Ubicacion geografica: "+ubicacionGeografica)
            p("Numero de interfaces: "+str(numInterfaces))
            p("Tiempo de actividad: "+tiempoActivo)
            p("Comunidad: "+comunidadAgente)
            p("IP: "+ipAgente)
            for grafica in graficas:
                div(img(src=grafica))
        
        with open('Reporte_'+ipAgente+'.html','w') as f:
            f.write(doc.render())

        pdfkit.from_file('Reporte_'+ipAgente+'.html','Reporte_'+ipAgente+'.pdf')

        input("Reporte creado\nENTER para continuar")
    else:
        os.system('clear')
        input("No hay agentes registrados")