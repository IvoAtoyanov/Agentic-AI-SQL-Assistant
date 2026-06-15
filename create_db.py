import sqlite3


conn=sqlite3.connect("shop.db")

cur=conn.cursor()


cur.execute(

"""

DROP TABLE IF EXISTS customers

"""

)


cur.execute(

"""

DROP TABLE IF EXISTS products

"""

)


cur.execute(

"""

DROP TABLE IF EXISTS orders

"""

)


cur.execute(

"""

CREATE TABLE customers(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,

city TEXT,

age INTEGER

)

"""

)



cur.execute(

"""

CREATE TABLE products(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,

price REAL

)

"""

)



cur.execute(

"""

CREATE TABLE orders(

id INTEGER PRIMARY KEY AUTOINCREMENT,

customer_id INTEGER,

product_id INTEGER,

quantity INTEGER

)

"""

)



customers=[

("Ivan","Sofia",25),

("Maria","Plovdiv",30),

("Georgi","Sofia",21),

("Petar","Varna",29),

("Anna","Sofia",34),

("Nikolay","Burgas",42)

]



products=[

("Laptop",2200),

("Mouse",40),

("Keyboard",90),

("Monitor",400),

("Headphones",120)

]



orders=[

(1,1,1),

(1,2,2),

(2,4,1),

(5,3,1),

(6,1,1)

]



cur.executemany(

"""

INSERT INTO customers(

name,

city,

age

)

VALUES

(?,?,?)

""",

customers

)



cur.executemany(

"""

INSERT INTO products(

name,

price

)

VALUES

(?,?)

""",

products

)



cur.executemany(

"""

INSERT INTO orders(

customer_id,

product_id,

quantity

)

VALUES

(?,?,?)

""",

orders

)


conn.commit()

conn.close()


print("Database created")
