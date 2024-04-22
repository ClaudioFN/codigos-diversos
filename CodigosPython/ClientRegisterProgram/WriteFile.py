"""
Created Date: 29/03/2024
Last Update: 21/04/2024
Description: Create the file to be used to register data
Methods: 
 1 - file_editing: edition and creation of the file
 1.1 - Enter parameters: new_file = identifies if it is a new file | file_name = name of the file | file_columns = name of each column of the file | 
                         client_details = class Client of details to be inserted in the file
"""
import Client
import csv

class WriteFile:
    def file_editing(new_file = "", file_path = "", file_name = "", file_columns = "", client_details = Client): 

        if not new_file:
            try:
                with open(file_path, 'w+') as file:
                    writer = csv.writer(file)
                    field = file_columns
                    
                    writer.writerow(field)
                    writer.writerow([client_details.cpf_cnpj, client_details.name, client_details.address, 
                                        client_details.neighborhood, client_details.city, client_details.state, 
                                        client_details.fu, client_details.main_phone, client_details.mobile_phone])
            except Exception as ex:
                print(f'An error has ocurred - creating the file: {str(ex)}')
            finally: 
                file.close()
        else:
            try:
                with open(file_path, 'a+') as file:
                    writer = csv.writer(file, lineterminator='\n')

                    writer.writerow([client_details.cpf_cnpj, client_details.name, client_details.address, 
                                        client_details.neighborhood, client_details.city, client_details.state, 
                                        client_details.fu, client_details.main_phone, client_details.mobile_phone])
            except Exception as ex:
                print(f'An error has ocurred - opening the file: {str(ex)}')   
            finally:
                file.close()