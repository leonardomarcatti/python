import mysql.connector

try:
    # Establish the connection
    mydb = mysql.connector.connect(
      host="172.17.0.3",
      user="root",
      password="a",
      database="banco" # Optional: specify a database
    )

    # Create a cursor object
    mycursor = mydb.cursor()

    # Execute an SQL query
    mycursor.execute("select * from users")

    # Fetch and print the results

    for users in mycursor:
        print(f'ID: {users[0]} -|-  Nome: {users[1]}')

    # Commit changes if any data was modified (e.g., INSERT, UPDATE)
    mydb.commit()

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
   mydb.close()
