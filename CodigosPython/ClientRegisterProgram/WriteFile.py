"""
Created Date: 29/03/2024
Last Update: 29/03/2024
Description: Create the file to be used to register data
"""
import Client
import csv

class WriteFile:
    def file_editing(new_file = "", file_name = "", file_columns = "", client_details = Client): 
        if not new_file:
            try:
                with open(file_name, 'w', newline='') as file:
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
                with open(file_name, 'a+') as file:
                    writer = csv.writer(file)

                    writer.writerow([client_details.cpf_cnpj, client_details.name, client_details.address, 
                                        client_details.neighborhood, client_details.city, client_details.state, 
                                        client_details.fu, client_details.main_phone, client_details.mobile_phone])
            except Exception as ex:
                print(f'An error has ocurred - opening the file: {str(ex)}')   
            finally:
                file.close()