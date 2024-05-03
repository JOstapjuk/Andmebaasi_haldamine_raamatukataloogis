from sqlite3 import connect, Error

def create_connection(path):
    connection = None
    try:
        connection = connect(path)
        print("Ühendus on edukalt tehtud")
    except Error as e:
        print("Tekkis viga", e, "")
    return connection

def execute_query(connection, query):
    try:
        global cursor
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud")
    except Error as e:
        print("Viga ", e, " tabeli loomisega")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print("Viga", e,"")

create_autor_table = """
CREATE TABLE IF NOT EXISTS Autorid (
    autor_id INTEGER PRIMARY KEY,
    autor_nimi TEXT NOT NULL,
    sünnikuupäev DATE NOT NULL
)
"""
create_zanr_table ="""
CREATE TABLE IF NOT EXISTS Žanrid (
    žanr_id INTEGER PRIMARY KEY,
    žanri_nimi TEXT NOT NULL
)
"""
create_raamatud_table = """
CREATE TABLE IF NOT EXISTS Raamatud (
    raamat_id INTEGER PRIMARY KEY,
    pealkiri TEXT NOT NULL,
    väljaandmise_kuupäev DATE NOT NULL,
    autor_id INTEGER,
    žanr_id INTEGER,
    FOREIGN KEY(autor_id) REFERENCES Autorid(autor_id),
    FOREIGN KEY(žanr_id) REFERENCES Žanrid(žanr_id)
)
"""

connection = create_connection(r"database.db")
#execute_query(connection, create_autor_table)

create_autor = "INSERT INTO Autorid VALUES (1, 'J.K. Rowling', '1965-07-31')"
create_autor = "INSERT INTO Autorid VALUES (2, 'George R.R. Martin', '1948-09-20')"
create_zanr = "INSERT INTO Žanrid VALUES (1, 'Fantaasia')"
create_zanr = "INSERT INTO Žanrid VALUES (2, 'Sci-Fi')"
create_raamatud = "INSERT INTO Raamatud VALUES (1, 'Harry Potter ja filosoofi kivi', '1997-06-26', 1, 1)"
create_raamatud = "INSERT INTO Raamatud VALUES (2, 'Troonide mäng', '1996-08-01', 2, 2)"
#execute_query(connection, create_raamatud)




select_Autorid = "SELECT * from Raamatud"
autorid = execute_read_query(connection, select_Autorid)
for autor in autorid:
    print(autor)





def add_autor_query(connection,user_data):
    query = "INSERT INTO Autorid(autor_id, autor_nimi, sünnikuupäev) VALUES ("+user_data")"
    execute_query(connection,query)

insert_autor = "'"+input("ID: ")+"','"+input("Nimi: ")+"','"+input("sünnikuupäev: ")+"'"
add_autor_query(connection,insert_autor)
#import tkinter as tk
#from tkinter import ttk

#def load_data():
#    cursor.execute("SELECT * FROM Raamatud")
#    data = cursor.fetchall()
#    for item in data:
#        tree.insert("", "end", values=item)

#root = tk.Tk()
#tree = ttk.Treeview(root, columns=("ID", "Title", "Author", "Genre"), show="headings")
#tree.heading("ID", text="ID")
#tree.heading("Title", text="Title")
#tree.heading("Author", text="Author")
#tree.heading("Genre", text="Genre")
#tree.pack()

#load_button = tk.Button(root, text="Load Data", command=load_data)
#load_button.pack()

#root.mainloop()
