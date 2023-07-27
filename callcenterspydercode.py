import datetime
import time
import random
import pyodbc

con = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-D9MU5PB\SQLEXPRESS;'
                        'Database=Call_Center;'
                        'Trusted_Connection=yes;')
cursor = con.cursor()

while True:
    date = datetime.date.today()
    location = random.randint(111, 201)
    company = random.randint(11, 30)
    issue = random.randint(111, 130)
    csr = random.randint(111, 210)
    rtime = random.randint(1, 300)
    ctime = random.randint(1, 600)
    status = random.randint(1, 4)
    if status == 1:
        rating = random.randint(5, 10)
    if status == 2:
        rating = random.randint(3, 8)
    if status == 3:
        rating = random.randint(1, 3)
    if status == 4:
        rating = random.randint(1, 5)

    print(date)
    cursor.execute('INSERT INTO calls VALUES (GETDATE(),'
                   + str(location) + ','
                   + str(company) + ','
                   + str(issue) + ','
                   + str(csr) + ','
                   + str(rtime) + ','
                   + str(ctime) + ','
                   + str(status) + ','
                   + str(rating) + ')')
    cursor.commit()
    time.sleep(0.1)
