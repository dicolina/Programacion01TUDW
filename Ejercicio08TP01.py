# 8. Escriba un programa que permita al usuario ingresar la base y altura de un triángulo para
# luego imprimir por pantalla la superficie total

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
superficie = (base * altura) / 2
print(f"La superficie del triángulo es: {superficie:.2f}")