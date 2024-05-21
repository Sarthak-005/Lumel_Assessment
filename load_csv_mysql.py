import csv
import mysql.connector

# Create a connection to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="saarRoot@5",
  database="Sales"
)

# Create a cursor object
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE Sales") 
# print("Database is created")

#Ccreate Table

mycursor.execute('CREATE TABLE IF NOT EXISTS Order (order_id INT NOT NULL ,Product_ID INT ,Quantity_Sold INT, Discount Float, Shipping_Cost Float,Date_of_Sale Date)')
#Open the CSV file
with open("order.csv", "r") as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)

    # Iterate over the rows in the CSV file
    for row in csvreader:
        # Insert the row data into the MySQL table
        mycursor.execute("INSERT INTO order (order_id,Product_ID,Quantity_Sold,Discount,Shipping_Cost,Date_of_Sale) VALUES (%s, %s, %s, %s, %s, %s)", row)

# Commit the changes to the database
mydb.commit()

# Close the cursor object
mycursor.close()

# # Close the connection to the database
mydb.close()