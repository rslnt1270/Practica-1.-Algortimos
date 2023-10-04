# Solicitar al usuario ingresar el tiempo en segundos
tiempo_en_segundos = int(input("Ingrese la cantidad de segundos: "))

# Calcular días, horas, minutos y segundos
dias = tiempo_en_segundos // 86400
horas = (tiempo_en_segundos % 86400) // 3600
minutos = ((tiempo_en_segundos % 86400) % 3600) // 60
segundos = ((tiempo_en_segundos % 86400) % 3600) % 60

# Crear el mensaje basado en los cálculos
mensaje = ""

if dias > 0:
    mensaje += f"{dias} día{'s' if dias > 1 else ''} "

if horas > 0:
    mensaje += f"{horas} hora{'s' if horas > 1 else ''} "

if minutos > 0:
    mensaje += f"{minutos} minuto{'s' if minutos > 1 else ''} "

if segundos > 0 or (dias == 0 and horas == 0 and minutos == 0):
    mensaje += f"{segundos} segundo{'s' if segundos > 1 else ''}"

# Mostrar el mensaje
print("El tiempo transcurrido es:", mensaje)