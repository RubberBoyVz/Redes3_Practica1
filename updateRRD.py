from datetime import datetime, timedelta
import rrdtool
from getSNMP import consultaSNMP

paquetesMulticast = 0
paquetesIP = 0
mensajesICMP = 0
segmentosRecibidos = 0
datagramasEntregados = 0

def iniciarActualizacion(comunidadAgente,ipAgente,interfaz,tiempoUsuario):
    tiempo_final = datetime.now() + timedelta(seconds=int(tiempoUsuario))
    while datetime.now() < tiempo_final:
        
        paquetesMulticast = int(
            consultaSNMP(comunidadAgente,ipAgente,
                         '1.3.6.1.2.1.2.2.1.12.' + interfaz))
        
        paquetesIP = int(
            consultaSNMP(comunidadAgente,ipAgente,
                         '1.3.6.1.2.1.4.3.0'))

        mensajesICMP = int(
            consultaSNMP(comunidadAgente,ipAgente,
                         '1.3.6.1.2.1.5.14.0'))

        segmentosRecibidos = int(
            consultaSNMP(comunidadAgente,ipAgente,
                         '1.3.6.1.2.1.6.10.0'))
        
        datagramasEntregados = int(
            consultaSNMP(comunidadAgente,ipAgente,
                         '1.3.6.1.2.1.7.1.0'))

        rrdtool.update("paquetesMulticast_" + ipAgente + ".rrd", "N:"+str(paquetesMulticast))
        rrdtool.update("paquetesIP_" + ipAgente + ".rrd", "N:"+str(paquetesIP))
        rrdtool.update("mensajesICMP_" + ipAgente + ".rrd", "N:"+str(mensajesICMP))
        rrdtool.update("segmentosRecibidos_" + ipAgente + ".rrd", "N:"+str(segmentosRecibidos))
        rrdtool.update("datagramasOut_" + ipAgente + ".rrd", "N:"+str(datagramasEntregados))