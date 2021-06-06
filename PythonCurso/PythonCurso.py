
import pyodbc
import Persona

print("1. Obtener")
op = input("Selecciona una opcion: ")

if op == "1":
    oPersona = Persona.clasePersona()
    oPersona.Obtener()
else:
    print("Opcion invalida")

