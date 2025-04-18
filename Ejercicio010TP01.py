# 10. Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al
# derecho que al revés. Por ejemplo: rayar, kayak, somos

texto = input("Ingrese un texto: ")
texto = texto.replace(" ", "").lower()  # Eliminar espacios y convertir a minúsculas
palindromo = texto == texto[::-1]  # Comparar el texto con su reverso
if palindromo:
    print(f"El texto '{texto}' es un palíndromo.")