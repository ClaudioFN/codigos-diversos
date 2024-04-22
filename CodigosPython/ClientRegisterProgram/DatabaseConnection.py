"""
Created Date: 21/04/2024
Last Update: 21/04/2024
Description: To establish the connection with the database
"""
import sqlite3
import Config as conf

class DatabaseConnection:

    def db_connection(): 
        connection_completed = False
        try:
            conn = sqlite3.connect(conf.DB_LOCATION + conf.DB_NAME)  

            connection_completed = True
        except:
            print(f'Fail to connect to the database {conf.DB_NAME}')

        if connection_completed:

            DatabaseConnection.db_create_table(conn)
        else:
            print(f'No connection was made!')
    
    # Create the table if it not exists
    def db_create_table(connection):

        try:
            connection.execute('CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY, name TEXT, cpf INTEGER, cnpj INTEGER, address TEXT, neighborhood TEXT ' + 
                            ', city TEXT, state TEXT, fu TEXT, phones TEXT)')
        except Exception as e:
            print(f'Error creating TABLE: {e}')
        finally:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * FROM people;
                """)
            for linha in cursor.fetchall():
                print(f'aqui: {linha}')
