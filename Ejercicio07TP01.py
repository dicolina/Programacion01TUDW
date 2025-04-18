# 7. Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y
# segundos son esos números de días.

dias = int(input("Ingrese la cantidad de días: "))
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60
print(f"{dias} días son {horas} horas, {minutos} minutos y {segundos} segundos.")