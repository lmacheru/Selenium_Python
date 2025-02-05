import mysql.connector

# insert_query = "insert into employees values(7, 'Homba', 'Maz', 456.80, '2026-11-06')"
update_query = "update employees set last_name = 'Mazaleni' where employee_id = 7"
delete_query = "delete from employees where employee_id = 6"

# Here we are connecting with the database
# Suppose your database is down, restarting or unavailable, this statement will throw an exception as a result of the database being unavailable
# That's why the wole code was put inside try block in order to handle the error
try:
    connection = mysql.connector.connect(host="localhost", port=3307, user="root", passwd="%LDMonyaku5995$", database="myDB")

    # create cursor, and through this cursor, an SQL statement will get executed
    cursor = connection.cursor()

    # Execute query through cursor
    cursor.execute("insert into employees values(7, 'Homba', 'Maz', 456.80, '2026-11-06')")
    cursor.execute(update_query)
    cursor.execute(delete_query)

    # Commit transaction
    connection.commit()

    # closing connection
    connection.close()

except:
    print("Connection unsuccessful...")
print("Finished.....")


# Database server ---> Is a storage where a data is stored
# Database client ---> Is a software through which we are able to connect with a database server
#                      So we are able to execute all these SQL commands through database client

# Why we communicate with the database, because we want to create tables, insert data, update data, delete, alter and select the data
# Here we are not testing the database, as we are not using selenium to interact with the database.
# So we needed to download/install "mysql-connector-python"