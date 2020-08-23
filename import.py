import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

drop = ''' DROP TABLE IF EXISTS books '''

sql ='''CREATE TABLE books(
   ISBN CHAR(50) NOT NULL,
   Title CHAR(50) NOT NULL,
   Author CHAR(50),
   Year CHAR(4)
)'''

db.execute(drop)

db.execute(sql)

with open('resources/books.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)
        db.execute("INSERT INTO books (ISBN, Title, Author, Year) VALUES (:ISBN, :Title, :Author, :Year)",
        {"ISBN": row[0], "Title": row[1], "Author": row[2], "Year": row[3]})

        print("Book Added !")

db.commit()
print("All Books have been successfully Added to the database !!")