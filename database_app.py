# create connection

import sqlite3
from datetime import datetime
 
 
DB_NAME = "retail_system.db"
 
 
def get_connection():
    return sqlite3.connect(DB_NAME)
 

# create tables function - define primary keys, foreign keys and constraints

 
def create_tables():
    connection = get_connection()
    cursor = connection.cursor()
 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT
    )
    """)
 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category_id INTEGER,
        price REAL NOT NULL,
        stock INTEGER NOT NULL,
        description TEXT,
        created_at TEXT,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
    """)
 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        email TEXT NOT NULL UNIQUE,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city TEXT,
        country TEXT,
        created_at TEXT
    )
    """)
    
    connection.commit()
    connection.close()


# add categories, add customers, add products functions

def add_category(name, description):
    connection = get_connection()
    cursor = connection.cursor()
 
    cursor.execute(
        "INSERT INTO categories (name, description) VALUES (?, ?)",
        (name, description)
    )
 
    connection.commit()
    connection.close()



def add_product(name, category_id, price, stock, description):
    connection = get_connection()
    cursor = connection.cursor()
 
    cursor.execute(
        """
        INSERT INTO products 
        (name, category_id, price, stock, description, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (name, category_id, price, stock, description, datetime.now().isoformat())
    )
 
    connection.commit()
    connection.close()



def add_customer(email, first_name, last_name, city, country):
    connection = get_connection()
    cursor = connection.cursor()
 
    cursor.execute(
        """
        INSERT INTO customers
        (email, first_name, last_name, city, country, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (email, first_name, last_name, city, country, datetime.now().isoformat())
    )
 
    connection.commit()
    connection.close()

# Fetching data from all table - get categories, get products, get customers

def get_categories():
    connection = get_connection()
    cursor = connection.cursor()
 
    cursor.execute("SELECT * FROM categories") #displays all columns of categories
    data = cursor.fetchall() 
 
    connection.close()
    return data

def get_customers():
    connection = get_connection()
    cursor = connection.cursor()
 
    cursor.execute("""
    SELECT *
    FROM customers
    """)
 
    data = cursor.fetchall()
    connection.close()
    return data

def get_products_with_categories():
    connection = get_connection()
    cursor = connection.cursor()
 
    cursor.execute("""
    SELECT products.id,
           products.name,
           categories.name,
           products.price,
           products.stock
    FROM products
    JOIN categories ON products.category_id = categories.id
    """)
 
    data = cursor.fetchall()
    connection.close()
    return data

if __name__ == "__main__":
    create_tables()

    # add_category("groceries", "salads&veggies")
    add_product("Oranges", 1, 2.99, 30, "fruits")
    add_customer("greeshma@gmail.com", "Greeshma", "Halesh", "Bangalore", "India")

 

    
 
 

 

 
 

 
 

 

 
 

 
# ---------- CUSTOMER FUNCTIONS ----------
 

 
 

 
 
# ---------- RUN ONCE ----------
 
