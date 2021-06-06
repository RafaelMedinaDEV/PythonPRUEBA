
import pyodbc
import Persona

print("1. Listar")
print("2. Insertar")
print("3. Actualizar")
print("4. Eliminar")

op = input("Selecciona una opcion: ")

if op == "1":
    oPersona = Persona.clasePersona()
    oPersona.Obtener()
if op == "2":
    oPersona = Persona.clasePersona()
    oPersona.Insertar()
else:
    print("Opcion no es correcta")


