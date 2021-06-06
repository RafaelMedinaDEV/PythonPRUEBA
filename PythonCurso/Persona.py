import pyodbc
class clasePersona:

    def Obtener(self):
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=.;'
                      'Database=CursoPython;'
                      'UID=sa;'
                      'PWD=sql')

        cursor = conn.cursor()
        cursor.execute('select * from persona')

        for row in cursor:
            print(row)

    def Insertar(self):
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=.;'
                      'Database=CursoPython;'
                      'UID=sa;'
                      'PWD=sql')
        nombre=input('Ingrese nombre: ')
        pais=input('Ingrese pais: ')
        
        query="Insert into Persona(Nombre,Pais) Values(?,?)"
        cursor = conn.cursor()

        cursor.execute(query, [nombre,pais])
        conn.commit()
        print('Guardado Exitosamente')
        conn.close()
        

        for row in cursor:
            print(row)