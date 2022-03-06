# sysdescr 1.3.6.1.2.1.1.1.0
# numero de interfaces de un agente 1.3.6.1.2.1.2.1.0
# descripcion interfaz "1.3.6.1.2.1.2.2.1.2."
# info admin interfaz "1.3.6.1.2.1.2.2.1.7."

# Paquetes multicast que ha recibido una interfaz 1.3.6.1.2.1.2.2.1.12.2
# Paquetes recibidos a protocolos IPv4, incluyendo los que tienen errores 1.3.6.1.2.1.4.3.0
# Mensajes ICMP echo que ha enviado el agente 1.3.6.1.2.1.5.14.0
# Segmentos recibidos, incluyendo los que se han recibido con errores 1.3.6.1.2.1.6.10.0
# Datagramas entregados a usuarios UDP 1.3.6.1.2.1.7.1.0

from visualizar import consultaSoloValor


if __name__ == '__main__':
    c = int(consultaSoloValor("comunidadASR","localhost","1.3.6.1.2.1.1.3.0"))
    print(str(int(c/100/60))+" minutos")