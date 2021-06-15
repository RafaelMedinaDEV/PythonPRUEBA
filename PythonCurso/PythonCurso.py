
import pyodbc
import Persona

print("PYTHON CRUD")
print("1. Listar")
print("2. Insertar")
print("3. Actualizar")
print("4. Eliminar")

op = input("Selecciona una opcion: ")

if op == "1":
    oPersona = Persona.clasePersona()
    oPersona.Obtener()
else:
    print("Opcion no es correcta")


