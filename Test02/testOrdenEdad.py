# 2. Escribe una función que tome una lista de objetos "Persona" y devuelva una lista con las personas mayores de edad (edad mayor o igual a 18) ordenadas alfabéticamente por su nombre.

# Definimos la clase Persona
class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

# Definimos la función "obtener_personas"
def obtener_personas():
  # Definimos el arreglo personas
  personas = []
    # Solicitamos los datos de personas por consola y los guardamos en el arreglo "persona"
  while True:
    nombre = input("Ingrese el nombre de la persona (o escriba 'salir' para terminar): ")
    if nombre.lower() == 'salir':
      break
    edad = int(input("Ingrese la edad de la persona: "))
    persona = Persona(nombre, edad)
    personas.append(persona)
  
  return personas

# Definimos la función "obtener_personas_mayores_edad" con el objetivo de filtrarlas
def obtener_personas_mayores_edad(personas):
  personas_mayores_edad = [persona for persona in personas if persona.edad >= 18]
  personas_mayores_edad.sort(key=lambda x: x.nombre)
  return personas_mayores_edad

# Realizamos el llamado a la función "obtener_personas" con el objetivo de obtener la lista de personas ingresadas
personas_ingresadas = obtener_personas()

# Imprimimos la lista de personas ingresadas sin filtros
print("\nPersonas ingresadas:")
for persona in personas_ingresadas:
  print(persona.nombre, persona.edad)

# Obtenemos y filtramos las personas mayores de edad
personas_mayores_edad = obtener_personas_mayores_edad(personas_ingresadas)

# Imprimir la lista de personas mayores de edad ordenadas alfabéticamente
print("\nPersonas mayores de edad ordenadas alfabéticamente:")
for persona in personas_mayores_edad:
  print(persona.nombre, persona.edad)