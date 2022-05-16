import sqlite3

def connect():
    connection = sqlite3.connect("library.db")
    conn = connection.cursor()
    conn.execute("CREATE TABLE IF NOT EXISTS library(id INTEGER PRIMARY KEY,title text,author text,year INTEGER,isbn INTEGER )")
    connection.commit()
    connection.close()

def insert(title,author,year,isbn):
    connection = sqlite3.connect("library.db")
    conn = connection.cursor()
    conn.execute("INSERT INTO library values(NULL,?,?,?,?)",(title,author,year,isbn))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("library.db")
    conn = connection.cursor()
    conn.execute("SELECT * FROM library")
    x = conn.fetchall()
    connection.commit()
    connection.close()
    return x

def search(title="",author="",year="",isbn=""):
    connection = sqlite3.connect("library.db")
    conn = connection.cursor()
    conn.execute("SELECT * FROM library WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    x = conn.fetchall()
    connection.commit()
    connection.close()
    return x

def update(id,title,author,year,isbn):
    connection = sqlite3.connect("library.db")
    conn = connection.cursor()
    conn.execute("UPDATE library SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    connection.commit()
    connection.close()

def delete(id):
    connection = sqlite3.connect("library.db")
    conn = connection.cursor()
    conn.execute("DELETE FROM library WHERE id=?",(id,))
    connection.commit()
    connection.close()

connect()



