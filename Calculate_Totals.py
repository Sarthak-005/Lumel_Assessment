from flask import Flask
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

app = Flask(__name__)

@app.route('/Revenue', methods=['GET'])
def get_total():
    mycursor.execute()