"""
Created Date: 23/07/2023
Last Update: 26/10/2024
Description: Connect and use data with MySQL
Observation: With logging to better locate errors and the basic instructions to use MySQL
"""
"""
Install the package: pip install mysql-connector-python
"""
import mysql.connector
from mysql.connector import Error
import logging
from datetime import datetime
"""
Configuration of the log archive
"""
logging.basicConfig(filename='DataManipulationMySQL_'+datetime.today().strftime('%d-%m-%Y')+'.log', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', level=0)
logging.info('\nBegging - '+ datetime.today().strftime('%d-%m-%Y %H:%M:%S'))
print('Begging - ', datetime.today().strftime('%d-%m-%Y %H:%M:%S'))
"""
 Connect to the MySQL Database
"""
DB_NAME = "test"
logging.info('Connecting to the MySQL')
POSITION = 0
try:
  POSITION = 10
  mydb = mysql.connector.connect(
    host="localhost-or-127.0.0.1",
    database="optional-database-name",
    port="optional-port",
    user="user-from-your-database",
    password="password-to-your-database"
  )
  POSITION = 20
  """
  Test if the connections were made and show some info
  """
  POSITION = 30
  if mydb.is_connected():
    POSITION = 40
    db_info = mydb.get_server_info()
    print("Connected to MySQL Server version: ", db_info)
    
    logging.info('Connection created successfully!')
    
    # Initialize the cursor
    POSITION = 50
    cursor = mydb.cursor()
    """
    Create the Database and Use It
    """
    # Check if the database exists before creating it
    POSITION = 60
    found_db = False
    cursor.execute("SHOW DATABASES")
    
    POSITION = 70
    for dbs in cursor:
      if dbs == DB_NAME:
        found_db = True
    
    POSITION = 80
    if found_db:
      print("Database exists! Just use it!")
    else :
        POSITION = 90
        print("Database "+DB_NAME+" doesn't exist, creating now...")
        
        POSITION = 100
        cursor.execute("CREATE DATABASE IF NOT EXISTS "+DB_NAME)
        print("Database "+DB_NAME+" created!")
        
    POSITION = 110
    cursor.execute("USE "+DB_NAME)
    
    # Make a select
    POSITION = 120
    cursor.execute("select database();")
    record = cursor.fetchone()
    # Show results
    print("You are connected to the ", record ," database.")
    
    logging.info('Database connected successfully!')
    """
    Creating a new table if not exists
    """
    POSITION = 130
    create_table = """CREATE TABLE IF NOT EXISTS notebook (
      id int(10) NOT NULL,
      company_name varchar(250) NOT NULL,
      product_name varchar(250) NOT NULL,
      price float NOT NULL,
      ram_memory varchar(50) NOT NULL,
      rom_memory varchar(50) NOT NULL,
      operational_sys varchar(50) NOT NULL,
      video_card varchar(100) NOT NULL,
      processor varchar(50) NOT NULL,
      total_available int(5),
      PRIMARY KEY (id)
      )"""
    POSITION = 140
    result_table_creation = cursor.execute(create_table)
    print("Notebook table created successfully! ", result_table_creation)
    
    
    logging.info('Table NOTEBOOK created successfully!')
    
    """
    Inserting data in the NOTEBOOK table
    """
    POSITION = 150
    insert_data = """ INSERT INTO notebook (
      id, company_name, product_name,
      price, ram_memory, rom_memory,
      operational_sys, video_card, processor,
      total_available
      ) 
      VALUES(
        1, 'LENOVO', 'Ideapad Gaming 3i',
        5.000, '8GB', '256GB',
        'Linux', 'NVIDIA GeForce GTX 1650 4GB', 'Intel Core i5-10300H',
        2
      )"""
    POSITION = 160
    cursor.execute(insert_data)
    
    POSITION = 150
    mydb.commit()
    print(cursor.rowcount, " - Data inserted successfully into the Notebook table!")
    
    logging.info('Data inserted in the table successfully!')
    
    """
    Select from the notebook table
    """
    POSITION = 170
    select_query = """ SELECT * FROM notebook """
    cursor.execute(select_query)
    
    POSITION = 180
    records = cursor.fetchall()
    print("Rows in the table: ", cursor.rowcount)
    
    logging.info('Data retrieved from the table successfully!')
    
    POSITION = 200
    print("\nShow data of each row: ")
    for row in records:
      print("ID = ", row[0])
      print("Company Name = ", row[1])
      print("Product Name = ", row[2])
      print("Price = ", row[3])
      print("Ram = ", row[4])
      print("Storage = ", row[5])
      print("Operational System = ", row[6])
      print("Video Card = ", row[7])
      print("Processor = ", row[8])
      print("Total Available = ", row[9], "\n")
  else:
    logging.info('Failed to connect!')
except Error as e:
  # Error found during connection process
  position_err = str(POSITION)
  logging.error("Something went wrong in the position "+position_err+": " + e.msg) 
  print("Error in the position ", POSITION,": ", e)
finally:
  if mydb.is_connected():
    cursor.close()
    mydb.close()
    print("MySQL connection closed!")
    
    logging.info('Connection closed successfully!')
  logging.info('Program DataManipulationMySQL is done!')
