from sqlite3 import connect, Error
from tkinter import messagebox
import tkinter as tk

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

# create_autor_table = """
# CREATE TABLE IF NOT EXISTS Autorid (
#    autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
#    autor_nimi TEXT NOT NULL,
#    sünnikuupäev DATE NOT NULL
# )
# """
# create_zanr_table ="""
# CREATE TABLE IF NOT EXISTS Žanrid (
#    žanr_id INTEGER PRIMARY KEY AUTOINCREMENT,
#    žanri_nimi TEXT NOT NULL
# )
#  """
# create_raamatud_table = """
# CREATE TABLE IF NOT EXISTS Raamatud (
#    raamat_id INTEGER PRIMARY KEY AUTOINCREMENT,
#    pealkiri TEXT NOT NULL,
#    väljaandmise_kuupäev DATE NOT NULL,
#    autor_id INTEGER,
#    žanr_id INTEGER,
#    FOREIGN KEY(autor_id) REFERENCES Autorid(autor_id),
#    FOREIGN KEY(žanr_id) REFERENCES Žanrid(žanr_id)
# )
# """

connection = create_connection(r"database.db")
# execute_query(connection, create_zanr_table)

# create_autor = "INSERT INTO Autorid(autor_nimi, sünnikuupäev) VALUES ('J.K. Rowling', '1965-07-31')"
# create_autor = "INSERT INTO Autorid VALUES (2, 'George R.R. Martin', '1948-09-20')"
# create_zanr = "INSERT INTO Žanrid VALUES (1, 'Fantaasia')"
# create_zanr = "INSERT INTO Žanrid VALUES (2, 'Sci-Fi')"
# create_raamatud = "INSERT INTO Raamatud VALUES (1, 'Harry Potter ja filosoofi kivi', '1997-06-26', 1, 1)"
# create_raamatud = "INSERT INTO Raamatud VALUES (2, 'Troonide mäng', '1996-08-01', 2, 2)"
# execute_query(connection, create_raamatud)


def add_autor_query(connection, user_data):
    query = "INSERT INTO Autorid(autor_nimi, sünnikuupäev) VALUES (?,?)"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()
    messagebox.showinfo("Edu","Autor lisas edukalt")

def add_zanr_query(connection, genre1):
    query = "INSERT INTO Žanrid(žanri_nimi) VALUES (?)"
    cursor = connection.cursor()
    cursor.execute(query, genre1)
    connection.commit()
    messagebox.showinfo("Edu", "Žanr lisatud edukalt")

def add_raamat_query(connection, user_data):
    query = "INSERT INTO Raamatud(pealkiri,väljaandmise_kuupäev,autor_id,žanr_id) VALUES (?,?,?,?)"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()
    messagebox.showinfo("Edu", "Raamat lisatud edukalt")

##insert_autor =(input("ID: "),input("Nimi: "),input("Sünnikuupäev: "))
##print(insert_autor)
##add_autor_query(connection,insert_autor)

##insert_zanr =(input("ID: "),input("Nimi: "))
##print(insert_zanr)
##add_zanr_query(connection,insert_zanr)

##insert_raamat =(input("ID: "),input("Pealkiri: "),input("Väljaandmise_kuupäev: "),input("Autor_ID: "),input("Žanr_ID: "))
##print(insert_raamat)
##add_raamat_query(connection,insert_raamat)





def update_autor_nimi(connection, user_data):
    query = "UPDATE Autorid SET autor_nimi = ? WHERE autor_nimi = ?"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()
    messagebox.showinfo("Edu", "Autori nimi uuendatud edukalt")


##update_autor_Nimi=(input("Uus autor nimi: "),input("ID: "))
##print(update_autor_Nimi)
##update_autor_nimi(connection,update_autor_Nimi)




def update_zanr_nimi(connection, user_data):
    query = "UPDATE Žanrid SET žanri_nimi = ? WHERE žanri_nimi = ?"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()
    messagebox.showinfo("Edu", "Genre nimi uuendatud edukalt")

##update_zanr_Nimi =(input("Uus žanr nimi: "),input("ID: "))
##print(update_zanr_Nimi)
##update_zanr_nimi(connection,update_zanr_Nimi)



def update_raamat_pealkiri(connection, user_data):
    query = "UPDATE Raamatud SET pealkiri = ? WHERE pealkiri = ?"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()
    messagebox.showinfo("Edu", "Raamatu pealkiri uuendatud edukalt")

##update_raamat_Pealkiri=(input("Uus raamat pealkiri: "),input("ID: "))
##print(update_raamat_Pealkiri)
##update_raamat_pealkiri(connection,update_raamat_Pealkiri)



def delete_raamat_pealkiri(connection, pealkiri):
    query = "DELETE FROM Raamatud WHERE pealkiri=?"
    cursor = connection.cursor()
    cursor.execute(query, (pealkiri,))
    connection.commit()
    messagebox.showinfo("Edu", "Raamat edukalt kustutatud")

def delete_genre_by_name_query(connection, genre_name):
    query = "DELETE FROM Žanrid WHERE žanri_nimi = ?"
    cursor = connection.cursor()
    cursor.execute(query, (genre_name,))
    connection.commit()
    messagebox.showinfo("Edu", "Žanr kustutatud edukalt")

def delete_autor_by_name(connection, autor_nimi):
    query = "DELETE FROM Autorid WHERE autor_nimi =?"
    cursor = connection.cursor()
    cursor.execute(query, (autor_nimi,))
    connection.commit()
    messagebox.showinfo("Edu", "Autor kustutatud edukalt")

##delete_raamat_autor = int(input("Autori nimi ID: "))
##delete_raamat_autorID(connection, (delete_raamat_autor,))

##delete_raamat_zanr = int(input("Enter the genre ID: "))
##delete_raamat_zanrID(connection, (delete_raamat_zanr,))


##all data show
allData = """
SELECT r.pealkiri, a.autor_nimi, z.žanri_nimi
FROM Raamatud r
INNER JOIN Autorid a ON r.autor_id = a.autor_id
INNER JOIN Žanrid z ON r.žanr_id = z.žanr_id;
"""
result = execute_read_query(connection, allData)
if result:
    for row in result:
        print(row)
else:
    print("No data found.")
    

def delete_tabel(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on kustatud")
        messagebox.showinfo("Success", "Tabel on kustatud")
    except Error as e:
        print("Viga ", e, " tabeli kustutamisega")
        messagebox.showerror("Error", f"Viga {e} tabeli kustutamisega")


