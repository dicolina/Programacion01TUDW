# 5. Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y
# luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente
# forma: “La respuesta es XX”.

print("Ingrese los números a sumar: ")
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

numero3 = float(input("Ingrese el numero a multiplicar: "))

suma = numero1 + numero2
multiplicacion = suma * numero3
print(f"La respuesta es {multiplicacion}")
