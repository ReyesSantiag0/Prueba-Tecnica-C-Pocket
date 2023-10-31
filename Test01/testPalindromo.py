# 1. Escribe una función que tome una cadena como entrada y devuelva true si la cadena es un palíndromo 
# (se lee igual de izquierda a derecha que de derecha a izquierda), o false en caso contrario.

#Pedimos al usuario que ingrese una cadena.
cadena = input("Hola, Ingresa una cadena: ")
#Definimos la función "cadena_palindromo" la cual recibe el parámetro "cadena" el cual contienen la cadena ingresada por el usuario.
def cadena_palindromo(cadena):
  # Eliminamos los espacios y convertimos la cadena a minúsculas.
  cadena_modificada = cadena.replace(" ", "").lower()
  # Comprobamos si la cadena ingresada por el usuario es palindromo o no lo es.
  print("¿La cadena " + cadena + " es palíndromo?")
  return cadena_modificada == cadena_modificada[::-1]

# Hacemos uso de la función "cadena_palindromo" recibiendo. 
print(cadena_palindromo(cadena))