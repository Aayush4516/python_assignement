import pandas as pd

import csv
import mysql.connector

connection= mysql.connector.connect(
      host="localhost",
      user="root",
      password="Aayush2019",
      database="employees"
    )

cursor= connection.cursor()

data={
      "Employee_id": [61, 12],
      "Email": ["nilay@gmail.com", "riya@gmail.com"],
      "Name": ["Nilay", "Riya"],
      "Phone":[9810971452,1122334455],
      "Pf_id":[111,112],
      "DOJ":["2021-06-06","2021-09-09"],
      "DOB":["2001-07-08","2000-09-23"],
      "Department":["HR","Technology"]
   }

df=pd.DataFrame(data)

df.to_csv('temp.csv', mode='a', index=False, header=False)

df = pd.read_csv('temp.csv')

with open('temp.csv', 'r') as file:
    csv_data = csv.reader(file)

    for row in csv_data:
        cursor.execute("INSERT INTO Employees (EmployeeId, Email, Name, Phone, PfId, DOJ, DOB, Department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",row)
      
connection.commit()


cursor.close()
connection.close()



