from sqlite3 import connect, Error
import tkinter as tk
from tkinter import messagebox

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

##create_autor_table = """
##CREATE TABLE IF NOT EXISTS Autorid (
##    autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
##    autor_nimi TEXT NOT NULL,
##    sünnikuupäev DATE NOT NULL
##)
##"""
##create_zanr_table ="""
##CREATE TABLE IF NOT EXISTS Žanrid (
##    žanr_id INTEGER PRIMARY KEY AUTOINCREMENT,
##    žanri_nimi TEXT NOT NULL
##)
##"""
##create_raamatud_table = """
##CREATE TABLE IF NOT EXISTS Raamatud (
##    raamat_id INTEGER PRIMARY KEY AUTOINCREMENT,
##    pealkiri TEXT NOT NULL,
##    väljaandmise_kuupäev DATE NOT NULL,
##    autor_id INTEGER,
##    žanr_id INTEGER,
##    FOREIGN KEY(autor_id) REFERENCES Autorid(autor_id),
##    FOREIGN KEY(žanr_id) REFERENCES Žanrid(žanr_id)
##)
##"""

connection = create_connection(r"database.db")
##execute_query(connection, create_raamatud_table)

##create_autor = "INSERT INTO Autorid(autor_nimi, sünnikuupäev) VALUES ('J.K. Rowling', '1965-07-31')"
##create_autor = "INSERT INTO Autorid VALUES (2, 'George R.R. Martin', '1948-09-20')"
##create_zanr = "INSERT INTO Žanrid VALUES (1, 'Fantaasia')"
##create_zanr = "INSERT INTO Žanrid VALUES (2, 'Sci-Fi')"
##create_raamatud = "INSERT INTO Raamatud VALUES (1, 'Harry Potter ja filosoofi kivi', '1997-06-26', 1, 1)"
##create_raamatud = "INSERT INTO Raamatud VALUES (2, 'Troonide mäng', '1996-08-01', 2, 2)"
##execute_query(connection, create_raamatud)



#select only one table 
select_Autorid = "SELECT * from Autorid"
autorid = execute_read_query(connection, select_Autorid)
for autor in autorid:
    print(autor)

##select_zanrid = "SELECT * from Žanrid"
##zanrid = execute_read_query(connection, select_zanrid)
##for zanr in zanrid:
##    print(zanr)

##select_raamatud = "SELECT * from Raamatud"
##raamatud = execute_read_query(connection, select_raamatud)
##for raamat in raamatud:
##    print(raamat)




def add_autor_query(connection,user_data):
    query = "INSERT INTO Autorid(autor_nimi, sünnikuupäev) VALUES (?,?)"
    cursor = connection.cursor()
    cursor.execute(query,user_data)
    connection.commit()

def add_zanr_query(connection,user_data):
    query = "INSERT INTO Žanrid(žanri_nimi) VALUES (?)"
    cursor = connection.cursor()
    cursor.execute(query,user_data)
    connection.commit()

def add_raamat_query(connection,user_data):
    query = "INSERT INTO Raamatud(pealkiri,väljaandmise_kuupäev,autor_id,žanr_id) VALUES (?,?,?,?)"
    cursor = connection.cursor()
    cursor.execute(query,user_data)
    connection.commit()

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
    query = "UPDATE Autorid SET autor_nimi =? WHERE autor_id =?"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()
def update_autor_sünnikuupäev(connection, user_data):
    query = "UPDATE Autorid SET sünnikuupäev =? WHERE autor_id =?"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()

##update_autor_Nimi=(input("Uus autor nimi: "),input("ID: "))
##print(update_autor_Nimi)
##update_autor_nimi(connection,update_autor_Nimi)

##update_autor_süünipäev=(input("Uus sünnipäev: "),input("ID: "))
##print(update_autor_süünipäev)
##update_autor_sünnikuupäev(connection,update_autor_süünipäev)



def update_zanr_nimi(connection,user_data):
    query = "UPDATE Žanrid SET žanri_nimi =? WHERE žanr_id =?"
    cursor = connection.cursor()
    cursor.execute(query, user_data)
    connection.commit()

##update_zanr_Nimi =(input("Uus žanr nimi: "),input("ID: "))
##print(update_zanr_Nimi)
##update_zanr_nimi(connection,update_zanr_Nimi)



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

##update_raamat_Pealkiri=(input("Uus raamat pealkiri: "),input("ID: "))
##print(update_raamat_Pealkiri)
##update_raamat_pealkiri(connection,update_raamat_Pealkiri)

##update_raamat_kuupäev=(input("Uus raamat väljaandmise kuupäev : "),input("ID: "))
##print(update_raamat_kuupäev)
##update_raamat_väljakuupäev(connection,update_raamat_kuupäev)

##update_raamat_autor_ID=(input("Uus raamat autor ID : "),input("ID: "))
##print(update_raamat_autor_ID)
##update_raamat_autorID(connection,update_raamat_autor_ID)

##update_raamat_žanr_ID=(input("Uus raamat žanr ID : "),input("ID: "))
##print(update_raamat_žanr_ID)
##update_raamat_žanrID(connection,update_raamat_žanr_ID)




def delete_raamat_autorID(connection,autor_ID):
    query = "DELETE FROM Raamatud WHERE autor_id = ?"
    cursor = connection.cursor()
    cursor.execute(query, autor_ID)
    connection.commit()

def delete_raamat_zanrID(connection,zanr_ID):
    query = "DELETE FROM Raamatud WHERE žanr_id = ?"
    cursor = connection.cursor()
    cursor.execute(query, zanr_ID)
    connection.commit()

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




def delete_tabel(connection,query):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on kustatud")
    except Error as e:
        print("Viga ",e," tabeli kustutamisega")


def update_author_name():
    author_id_entry = tk.Entry(root)
    new_name_entry = tk.Entry(root)
    author_id = author_id_entry.get()
    new_name = new_name_entry.get()
    update_autor_nimi(connection, (new_name, author_id))

def update_author_birthdate():
    author_id_entry = tk.Entry(root)
    new_birthdate_entry = tk.Entry(root)
    author_id = author_id_entry.get()
    new_birthdate = new_birthdate_entry.get()
    update_autor_sünnikuupäev(connection, (new_birthdate, author_id))

def update_genre_name():
    genre_id_entry = tk.Entry(root)
    new_name_entry = tk.Entry(root)
    genre_id = genre_id_entry.get()
    new_name = new_name_entry.get()
    update_zanr_nimi(connection, (new_name, genre_id))

def update_book_title():
    book_id_entry = tk.Entry(root)
    new_title_entry = tk.Entry(root)
    book_id = book_id_entry.get()
    new_title = new_title_entry.get()
    update_raamat_pealkiri(connection, (new_title, book_id))

def update_book_release_date():
    book_id_entry = tk.Entry(root)
    new_release_date_entry = tk.Entry(root)
    book_id = book_id_entry.get()
    new_release_date = new_release_date_entry.get()
    update_raamat_väljakuupäev(connection, (new_release_date, book_id))

def update_book_author_id():
    book_id_entry = tk.Entry(root)
    new_author_id_entry = tk.Entry(root)
    book_id = book_id_entry.get()
    new_author_id = new_author_id_entry.get()
    update_raamat_autorID(connection, (new_author_id, book_id))

def update_book_genre_id():
    book_id_entry = tk.Entry(root)
    new_genre_id_entry = tk.Entry(root)
    book_id = book_id_entry.get()
    new_genre_id = new_genre_id_entry.get()
    update_raamat_žanrID(connection, (new_genre_id, book_id))

def add_author():
    author_data_entry = tk.Entry(root)
    author_data_entry.focus_set()
    author_data_frame = tk.Toplevel(root)
    author_data_frame.title("Lisa autor")
    tk.Label(author_data_frame, text="Autori nimi:").grid(row=1, column=0)
    author_name_entry = tk.Entry(author_data_frame)
    author_name_entry.grid(row=1, column=1)
    tk.Label(author_data_frame, text="Sünnipäev:").grid(row=2, column=0)
    author_birthdate_entry = tk.Entry(author_data_frame)
    author_birthdate_entry.grid(row=2, column=1)
    
    def add_author_to_database():
        author_data = ( author_name_entry.get(), author_birthdate_entry.get())
        add_autor_query(connection, author_data)
        author_data_frame.destroy()
    
    add_btn = tk.Button(author_data_frame, text="Lisa autor", command=add_author_to_database)
    add_btn.grid(row=3, column=0, columnspan=2)

def add_genre():
    genre_data_entry = tk.Entry(root)
    genre_data_entry.focus_set()
    genre_data_frame = tk.Toplevel(root)
    genre_data_frame.title("Lisa žanr")
    tk.Label(genre_data_frame, text="Žanr nimi:").grid(row=1, column=0)
    genre_name_entry = tk.Entry(genre_data_frame)
    genre_name_entry.grid(row=1, column=1)
    
    def add_genre_to_database():
        genre_data = (genre_name_entry.get())
        add_zanr_query(connection, genre_data)
        genre_data_frame.destroy()
    
    add_btn = tk.Button(genre_data_frame, text="Lisa žanr", command=add_genre_to_database)
    add_btn.grid(row=2, column=0, columnspan=2)

def add_book():
    book_data_entry = tk.Entry(root)
    book_data_entry.focus_set()
    book_data_frame = tk.Toplevel(root)
    book_data_frame.title("Lisa raamat")
    tk.Label(book_data_frame, text="Pealkiri:").grid(row=1, column=0)
    title_entry = tk.Entry(book_data_frame)
    title_entry.grid(row=1, column=1)
    tk.Label(book_data_frame, text="Väljaandmise kuupäev:").grid(row=2, column=0)
    release_date_entry = tk.Entry(book_data_frame)
    release_date_entry.grid(row=2, column=1)
    tk.Label(book_data_frame, text="Autor ID:").grid(row=3, column=0)
    author_id_entry = tk.Entry(book_data_frame)
    author_id_entry.grid(row=3, column=1)
    tk.Label(book_data_frame, text="Žanr ID:").grid(row=4, column=0)
    genre_id_entry = tk.Entry(book_data_frame)
    genre_id_entry.grid(row=4, column=1)
    
    def add_book_to_database():
        book_data = (title_entry.get(), release_date_entry.get(), 
                     author_id_entry.get(), genre_id_entry.get())
        add_raamat_query(connection, book_data)
        book_data_frame.destroy()
    
    add_btn = tk.Button(book_data_frame, text="Lisa raamat", command=add_book_to_database)
    add_btn.grid(row=5, column=0, columnspan=2)

def delete_book_by_author():
    author_id_entry = tk.Entry(root)
    author_id_entry.focus_set()
    author_id = author_id_entry.get()
    delete_raamat_autorID(connection, (author_id,))

def delete_book_by_genre():
    genre_id_entry = tk.Entry(root)
    genre_id_entry.focus_set()
    genre_id = genre_id_entry.get()
    delete_raamat_zanrID(connection, (genre_id,))

def show_all_data():
    allData = """
    SELECT r.pealkiri, a.autor_nimi, z.žanri_nimi
    FROM Raamatud r
    INNER JOIN Autorid a ON r.autor_id = a.autor_id
    INNER JOIN Žanrid z ON r.žanr_id = z.žanr_id;
    """
    result = execute_read_query(connection, allData)
    if result:
        data_window = tk.Toplevel(root)
        data_window.title("Kõik andmed")
        
        text_widget = tk.Text(data_window, width=40, height=10)
        text_widget.pack()
        
        for row in result:
            text_widget.insert(tk.END, f"{row}\n")
    else:
        print("Andmeid ei leitud")


root = tk.Tk()
root.title("Raamatukataloog")

update_buttons_frame = tk.Frame(root)
update_buttons_frame.pack(pady=10)

frame1 = tk.Frame(root)
frame1.pack(pady=10)

frame2 = tk.Frame(root)
frame2.pack(pady=10)

frame3 = tk.Frame(root)
frame3.pack(pady=10)

frame4 = tk.Frame(root)
frame4.pack(pady=10)

update_name_btn = tk.Button(frame1, text="Uuenda autori nime", command=update_author_name)
update_name_btn.pack()

update_birthdate_btn = tk.Button(frame1, text="Uuenda autori sünnikuupäeva", command=update_author_birthdate)
update_birthdate_btn.pack()

add_author_btn = tk.Button(frame1, text="Lisa autor", command=add_author)
add_author_btn.pack()

add_genre_btn = tk.Button(frame2, text="Lisa žanr", command=add_genre)
add_genre_btn.pack()

add_book_btn = tk.Button(frame3, text="Lisa raamat", command=add_book)
add_book_btn.pack()

delete_book_author_btn = tk.Button(frame4, text="Kustuta raamat autori poolt", command=delete_book_by_author)
delete_book_author_btn.pack(side=tk.LEFT)

delete_book_genre_btn = tk.Button(frame4, text="Kustuta raamat žanri järgi", command=delete_book_by_genre)
delete_book_genre_btn.pack(side=tk.LEFT)

show_data_frame = tk.Frame(root)
show_data_frame.pack(pady=10)

show_data_btn = tk.Button(show_data_frame, text="Näita kõiki andmeid", command=show_all_data)
show_data_btn.pack()

root.mainloop()
