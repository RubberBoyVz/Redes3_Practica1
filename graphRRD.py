import rrdtool
import time

tiempo_actual = int(time.time())
tiempo_inicial = tiempo_actual - 600

def CrearGraficas(ipAgente):
    ret1 = rrdtool.graph( "paquetesMulticast_" + ipAgente + ".png",
                         "--start",str(tiempo_inicial),
                         "--end","N",
                         "--vertical-label=Paquetes",
                         "--title=Paquetes multicast que ha\nrecibido una interfaz",
                         "DEF:paquetesMulticast=paquetesMulticast_" + ipAgente + ".rrd:paquetesMulticast:AVERAGE",
                         "LINE3:paquetesMulticast#0000FF:Paquetes Multicast")
    
    ret2 = rrdtool.graph( "paquetesIP_" + ipAgente + ".png",
                         "--start",str(tiempo_inicial),
                         "--end","N",
                         "--vertical-label=Paquetes",
                         "--title=Paquetes recibidos a protocolos IPv4",
                         "DEF:paquetesIP=paquetesIP_" + ipAgente + ".rrd:paquetesIP:AVERAGE",
                         "LINE3:paquetesIP#C800FF:Paquetes IP")

    ret3 = rrdtool.graph( "mensajesICMP_" + ipAgente + ".png",
                         "--start",str(tiempo_inicial),
                         "--end","N",
                         "--vertical-label=Mensajes",
                         "--title=Mensajes ICMP echo que ha\nenviado el agente",
                         "DEF:mensajesICMP=mensajesICMP_" + ipAgente + ".rrd:mensajesICMP:AVERAGE",
                         "LINE3:mensajesICMP#B82411:Mensajes ICMP")

    ret4 = rrdtool.graph( "segmentosRecibidos_" + ipAgente + ".png",
                         "--start",str(tiempo_inicial),
                         "--end","N",
                         "--vertical-label=Segmentos",
                         "--title=Segmentos recibidos\nincluyendo los que se han recibido con errores",
                         "DEF:segmentosRecibidos=segmentosRecibidos_" + ipAgente + ".rrd:segmentosRecibidos:AVERAGE",
                         "LINE3:segmentosRecibidos#6AB811:Segmentos Recibidos")
    
    ret5 = rrdtool.graph( "datagramasOut_" + ipAgente + ".png",
                         "--start",str(tiempo_inicial),
                         "--end","N",
                         "--vertical-label=Datagramas",
                         "--title=Datagramas entregados a\nusuarios UDP",
                         "DEF:datagramasOut=datagramasOut_" + ipAgente + ".rrd:datagramasOut:AVERAGE",
                         "LINE3:datagramasOut#6AB811:Datagramas Entregados")
