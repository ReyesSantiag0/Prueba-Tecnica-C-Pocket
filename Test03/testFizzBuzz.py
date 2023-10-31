# 3. Escribe una función que tome un número entero como entrada y devuelva "Fizz" si el número es divisible por 3, "Buzz" si es divisible por 5, y "FizzBuzz" si es divisible por ambos. Si no es divisible por ninguno de ellos, la función debe devolver el número como una cadena.

# Utilizamos try-except para el manejo de control de errores
try:
    # Pedimos al usuario que ingrese una cadena.
    numero = input("Hola, Ingresa un número entero: ")
    # Convertimos la entrada del usuario a un número entero.
    numero_entero = int(numero)
    
    # Definimos la función "fizz_buzz" para determinar la divisibilidad del número ingresado.
    def fizz_buzz(numero_entero): 
      if numero_entero % 3 == 0 and numero_entero % 5 == 0:
        return "FizzBuzz"
      elif numero_entero % 3 == 0:
        return "Fizz"
      elif numero_entero % 5 == 0:
        return "Buzz"
      else:
        return str(numero_entero)

    resultado = fizz_buzz(numero_entero)
    print(resultado)

except ValueError:
    print("El valor ingresado no es un número entero.")

