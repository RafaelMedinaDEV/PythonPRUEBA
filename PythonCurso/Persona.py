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