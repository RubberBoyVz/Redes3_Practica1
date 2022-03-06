from datetime import date

fechaNacimiento = date(1997,6,24)
fechaActual = date(2022,2,23)

diasVividos = fechaActual - fechaNacimiento
bloque = (diasVividos.days % 3) + 1

print("Bloque asignado:",bloque)