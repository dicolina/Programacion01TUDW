# 12. Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla el
# día, mes y año. Ej:
# Usuario ingresa: 17/05/1985
# Programa imprime: Día: 17, Mes: 05 y Año: 1985


# Solicitar al usuario que ingrese una fecha en formato dd/mm/aaaa
fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
# dia = fecha[0:2]
# mes = fecha[3:5]
# anio = fecha[6:10]
# Imprimir el día, mes y año en pantalla    
print(f"Dia: {fecha[0:2]}, Mes: {fecha[3:5]} y Año: {fecha[6:10]}")

