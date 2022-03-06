from genericpath import exists
from time import sleep
import rrdtool
import os

def crearBasesDeDatos(ipAgente):
    crearBase1(ipAgente)
    crearBase2(ipAgente)
    crearBase3(ipAgente)
    crearBase4(ipAgente)
    crearBase5(ipAgente)

def crearBase1(ipAgente):
    ret1 = rrdtool.create("paquetesMulticast_" + ipAgente + ".rrd",
                         "--start",'N',
                         "--step",'60',
                         "DS:paquetesMulticast:COUNTER:120:U:U",
                         "RRA:AVERAGE:0.5:1:100")
    if ret1:
        print (rrdtool.error())

def crearBase2(ipAgente):
    ret2 = rrdtool.create("paquetesIP_" + ipAgente + ".rrd",
                         "--start",'N',
                         "--step",'60',
                         "DS:paquetesIP:COUNTER:120:U:U",
                         "RRA:AVERAGE:0.5:1:100")
    if ret2:
        print (rrdtool.error())

def crearBase3(ipAgente):
    ret3 = rrdtool.create("mensajesICMP_" + ipAgente + ".rrd",
                         "--start",'N',
                         "--step",'60',
                         "DS:mensajesICMP:COUNTER:120:U:U",
                         "RRA:AVERAGE:0.5:1:100")                    
    if ret3:
        print (rrdtool.error())

def crearBase4(ipAgente):
    ret4 = rrdtool.create("segmentosRecibidos_" + ipAgente + ".rrd",
                         "--start",'N',
                         "--step",'60',
                         "DS:segmentosRecibidos:COUNTER:120:U:U",
                         "RRA:AVERAGE:0.5:1:100")
    if ret4:
        print (rrdtool.error())

def crearBase5(ipAgente):
    ret5 = rrdtool.create("datagramasOut_" + ipAgente + ".rrd",
                         "--start",'N',
                         "--step",'60',
                         "DS:datagramasOut:COUNTER:120:U:U",
                         "RRA:AVERAGE:0.5:1:100")
    if ret5:
        print (rrdtool.error())

def eliminarArchivos(ipAgente):
    if exists("paquetesMulticast_" + ipAgente + ".rrd"):
        os.remove("paquetesMulticast_" + ipAgente + ".rrd")
    if exists("paquetesMulticast_" + ipAgente + ".png"):
        os.remove("paquetesMulticast_" + ipAgente + ".png")
    if exists("paquetesIP_" + ipAgente + ".rrd"):
        os.remove("paquetesIP_" + ipAgente + ".rrd")
    if exists("paquetesIP_" + ipAgente + ".png"):
        os.remove("paquetesIP_" + ipAgente + ".png")
    if exists("mensajesICMP_" + ipAgente + ".rrd"):
        os.remove("mensajesICMP_" + ipAgente + ".rrd")
    if exists("mensajesICMP_" + ipAgente + ".png"):
        os.remove("mensajesICMP_" + ipAgente + ".png")
    if exists("segmentosRecibidos_" + ipAgente + ".rrd"):
        os.remove("segmentosRecibidos_" + ipAgente + ".rrd")
    if exists("segmentosRecibidos_" + ipAgente + ".png"):
        os.remove("segmentosRecibidos_" + ipAgente + ".png")
    if exists("datagramasOut_" + ipAgente + ".rrd"):
        os.remove("datagramasOut_" + ipAgente + ".rrd")
    if exists("datagramasOut_" + ipAgente + ".png"):
        os.remove("datagramasOut_" + ipAgente + ".png")
    if exists("Reporte_" + ipAgente + ".html"):
        os.remove("Reporte_" + ipAgente + ".html")
    if exists("Reporte_" + ipAgente + ".pdf"):
        os.remove("Reporte_" + ipAgente + ".pdf")

