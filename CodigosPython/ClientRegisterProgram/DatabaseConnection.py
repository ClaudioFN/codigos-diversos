"""
Created Date: 21/04/2024
Last Update: 23/04/2024
Description: To establish the connection with the database e execute others actions
"""
import sqlite3
import Config as conf

class DatabaseConnection:

    def db_connection(): 
        connection_completed = False
        try:
            conn = sqlite3.connect(conf.DB_LOCATION + conf.DB_NAME)  

            connection_completed = True
        except Exception as e:
            print(f'Fail to connect to the database {conf.DB_NAME}: {e}')
            return
        # Creating table if not exists 
        try:
            cur.execute("""SELECT * FROM people""")
            cur = conn.cursor() 
            data_list_test = cur.fetchall() 
        except:
            print('Table people not found. Creating the table now.')
            if connection_completed:
                DatabaseConnection.db_create_table(conn)
                return conn
            else:
                print(f'No connection was made!')
        return conn
    # Method to Create the table people
    def db_create_table(connection):
        try:
            #connection.execute("DROP TABLE people")
            connection.execute('CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY, name TEXT, cpf INTEGER, cnpj INTEGER, address TEXT, neighborhood TEXT ' + 
                               ', city TEXT, state TEXT, fu TEXT, main_phone TEXT, mobile_phone TEXT)')
        except Exception as e:
            print(f'Error creating TABLE: {e}')


    def db_insert_data(connection, client_data):
        posicao_erro = ''
        try:
            cpf_data = ''
            cnpj_data = ''
            if len(client_data.cpf_cnpj) <= 11: 
                cpf_data = client_data.cpf_cnpj 
            else:
                cnpj_data = client_data.cpf_cnpj
            posicao_erro = '1'
            cursor = connection.cursor()
            cursor.execute("""
                SELECT max(id) FROM people;
                """)
            posicao_erro = '2'
            for linha in cursor.fetchall():
                max_id = linha[0]

            posicao_erro = '3'
            print(f'tupla: {max_id}')
            if max_id != '':
                max_id = str(int(max_id)+1)
            else: 
                max_id = 1
            posicao_erro = '3.5'
            data_tuple = (max_id, client_data.name, cpf_data, cnpj_data, client_data.address, client_data.neighborhood, client_data.city
                          , client_data.state, client_data.fu, client_data.main_phone, client_data.mobile_phone)
            posicao_erro = '4'
            insert_instruction = """INSERT INTO people (id, name, cpf, cnpj, address, neighborhood, city, state, fu, main_phone, mobile_phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            posicao_erro = '5'
            cursor.execute(insert_instruction, data_tuple)
            posicao_erro = '6'
            connection.commit()
            print('Data included!')
        except Exception as e:
            print(f'Error during insert in TABLE - {posicao_erro}: {e}')
        finally:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * FROM people;
                """)
            for linha in cursor.fetchall():
                print(f'aqui: {linha}')