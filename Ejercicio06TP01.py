# 6. Programe una aplicación de consola que pregunte el precio total de la cuenta, luego
# pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el
# número de comensales y mostrar cuánto debe pagar cada persona.

total = float(input("Ingrese el precio total de la cuenta $: "))
comensales = int(input("Ingrese la cantidad de comensales: "))
pago_por_persona = total / comensales
print(f"Cada persona debe pagar: {pago_por_persona:.2f}")