#Importamos el modulo de fecha
import datetime

#Ingeso de datos
fecha_nacimiento = input('Ingrese su fecha de nacimiento (dd/mm/yyyy): ')
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
hoy = datetime.datetime.today().date()

#Calculo de edad
edad = hoy.year - fecha_nacimiento.year
verificacion_mes = hoy.month - fecha_nacimiento.month
verificacion_fecha = hoy.day - fecha_nacimiento.day

#Convertimos los valores de las variables a int
edad = int(edad)
verificacion_mes = int(verificacion_mes)
verificacion_fecha = int(verificacion_fecha)

#Validacion si ya cumpliste años
if verificacion_mes < 0 :
    edad = edad-1
elif verificacion_fecha < 0 and verificacion_mes == 0:
    edad = edad-1

#Imprime la edad
print("Tu edad es:",edad, "años")