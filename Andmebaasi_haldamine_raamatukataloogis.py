from sqlite3 import connect, Error
from turtle import update

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
    query = "INSERT INTO Autorid(autor_id, autor_nimi, sünnikuupäev) VALUES (?,?,?)"
    cursor = connection.cursor()
    cursor.execute(query,user_data)
    connection.commit()

def add_zanr_query(connection,user_data):
    query = "INSERT INTO Žanrid(žanr_id, žanri_nimi) VALUES (?,?)"
    cursor = connection.cursor()
    cursor.execute(query,user_data)
    connection.commit()

def add_raamat_query(connection,user_data):
    query = "INSERT INTO Raamatud(raamat_id,pealkiri,väljaandmise_kuupäev,autor_id,žanr_id) VALUES (?,?,?,?,?)"
    cursor = connection.cursor()
    cursor.execute(query,user_data)
    connection.commit()

#insert_autor =(input("ID: "),input("Nimi: "),input("Sünnikuupäev: "))
#print(insert_autor)
#add_autor_query(connection,insert_autor)

#insert_zanr =(input("ID: "),input("Nimi: "))
#print(insert_zanr)
#add_zanr_query(connection,insert_zanr)

#insert_raamat =(input("ID: "),input("Pealkiri: "),input("Väljaandmise_kuupäev: "),input("Autor_ID: "),input("Žanr_ID: "))
#print(insert_raamat)
#add_raamat_query(connection,insert_raamat)


def update_autor_nimi(connection, user_data):
    query = "UPDATE Autorid SET autor_nimi =? WHERE autor_id =?"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()
def update_autor_sünnikuupäev(connection, user_data):
    query = "UPDATE Autorid SET sünnikuupäev =? WHERE autor_id =?"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()

#update_autor_Nimi=(input("Uus autor nimi: "),input("ID: "))
#print(update_autor_Nimi)
#update_autor_nimi(connection,update_autor_Nimi)

#update_autor_süünipäev=(input("Uus sünnipäev: "),input("ID: "))
#print(update_autor_süünipäev)
#update_autor_sünnikuupäev(connection,update_autor_süünipäev)

def update_zanr_nimi(connection,user_data):
    query = "UPDATE Žanrid SET žanri_nimi =? WHERE žanr_id =?"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()

#update_zanr_Nimi =(input("Uus žanr nimi: "),input("ID: "))
#print(update_zanr_Nimi)
#update_zanr_nimi(connection,update_zanr_Nimi)

def update_raamat_pealkiri(connection, user_data):
    query = "UPDATE Raamatud SET pealkiri =? WHERE raamat_id =?"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()

def update_raamat_väljakuupäev(connection, user_data):
    query = "UPDATE Raamatud SET väljaandmise_kuupäev =? WHERE raamat_id =?"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()

def update_raamat_autorID(connection, user_data):
    query = "UPDATE Raamatud SET autor_id =? WHERE raamat_id =?"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()

def update_raamat_žanrID(connection, user_data):
    query = "UPDATE Raamatud SET žanr_id =? WHERE raamat_id =?"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()

#update_raamat_Pealkiri=(input("Uus raamat pealkiri: "),input("ID: "))
#print(update_raamat_Pealkiri)
#update_raamat_pealkiri(connection,update_raamat_Pealkiri)

update_raamat_kuupäev=(input("Uus raamat väljaandmise kuupäev : "),input("ID: "))
print(update_raamat_kuupäev)
update_raamat_pealkiri(connection,update_raamat_kuupäev)