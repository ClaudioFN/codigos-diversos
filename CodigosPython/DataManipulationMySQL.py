
"""
Install the package: pip install mysql-connector-python
"""
import mysql.connector
from mysql.connector import Error
"""
 Connect to the MySQL Database
"""
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
    
    # Initialize the cursor
    POSITION = 50
    cursor = mydb.cursor()

    """
    Create the Database and Use Database
    """
    POSITION = 55
    cursor.execute("CREATE DATABASE the-name-of-your-database")

    POSITION = 60
    cursor.execute("USE the-name-of-your-database")
    
    # Make a select
    POSITION = 60
    cursor.execute("select database();")
    record = cursor.fetchone()
    # Show results
    print("You are connected to the ", record ," database.")
    
    """
    Creating a new table if not exists
    """
    POSITION = 70
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
    POSITION = 80
    result_table_creation = cursor.execute(create_table)
    print("Notebook table created successfully! ", result_table_creation)
    
    """
    Inserting data in the NOTEBOOK table
    """
    POSITION = 90
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
    POSITION = 100
    cursor.execute(insert_data)
    
    POSITION = 110
    mydb.commit()
    print(cursor.rowcount, " - Data inserted successfully into the Notebook table!")
    
    """
    Select from the notebook table
    """
    POSITION = 120
    select_query = """ SELECT * FROM notebook """
    cursor.execute(select_query)
    
    POSITION = 130
    records = cursor.fetchall()
    print("Rows in the table: ", cursor.rowcount)
    
    POSITION = 140
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
    
except Error as e:
  # Error found during connection process
  print("Error in the position", POSITION,": ", e)
finally:
  if mydb.is_connected():
    cursor.close()
    mydb.close()
    print("MySQL connection closed!")
