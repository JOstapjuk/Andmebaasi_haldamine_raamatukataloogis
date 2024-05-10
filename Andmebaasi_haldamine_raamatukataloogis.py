from tkinter import ttk
import tkinter as tk
from tkinter.constants import CENTER, END
from tkinter import messagebox
from def_raamat import *


def update_autor_nimi2():
    autor_nimi = valitud_autor_nimi.get()
    uus_nimi = uus_nimi_entry.get()
    update_autor_nimi(connection, (uus_nimi, autor_nimi))
    uus_nimi_entry.delete(0, END)

def update_zanr_nimi2():
    zanr_nimi = valitud_zanr_nimi.get()
    uus_nimi = uus_zanr_nimi_entry.get()
    update_zanr_nimi(connection, (uus_nimi, zanr_nimi))
    uus_zanr_nimi_entry.delete(0, END)

def update_raamat_pealkiri2():
    raamat_pealkiri = valitud_raamat_pealkiri.get()
    uus_pealkiri = uus_pealkiri_entry.get()
    update_raamat_pealkiri(connection, (uus_pealkiri, raamat_pealkiri))
    uus_pealkiri_entry.delete(0, END)

def add_autor():
    autor_andmed_entry = tk.Entry(root)
    autor_andmed_entry.focus_set()
    autor_andmed_frame = tk.Toplevel(root)
    autor_andmed_frame.title("Lisa autor")
    tk.Label(autor_andmed_frame, text="Autori nimi:").grid(row=1, column=0)
    autor_nimi_entry = tk.Entry(autor_andmed_frame)
    autor_nimi_entry.grid(row=1, column=1)
    tk.Label(autor_andmed_frame, text="Sünnipäev:").grid(row=2, column=0)
    autor_sünnipäev_entry = tk.Entry(autor_andmed_frame)
    autor_sünnipäev_entry.grid(row=2, column=1)
    
    def add_autor_andmebaasi():
        autor_andmed = ( autor_nimi_entry.get(), autor_sünnipäev_entry.get())
        add_autor_query(connection, autor_andmed)
        autor_andmed_frame.destroy()
    
    add_btn = tk.Button(autor_andmed_frame, text="Lisa autor", command=add_autor_andmebaasi)
    add_btn.grid(row=3, column=0, columnspan=2)

def add_zanr():
    zanr_andmed_entry = tk.Entry(root)
    zanr_andmed_entry.focus_set()
    zanr_andmed_frame = tk.Toplevel(root)
    zanr_andmed_frame.title("Lisa žanr")
    tk.Label(zanr_andmed_frame, text="Žanr nimi:").grid(row=1, column=0)
    zanr_nimi_entry = tk.Entry(zanr_andmed_frame)
    zanr_nimi_entry.grid(row=1, column=1)
    
    def add_zanr_andmebaasi():
        zanr_data = (zanr_nimi_entry.get(),)
        add_zanr_query(connection, zanr_data)
        zanr_andmed_frame.destroy()
    
    add_btn = tk.Button(zanr_andmed_frame, text="Lisa žanr", command=add_zanr_andmebaasi)
    add_btn.grid(row=2, column=0, columnspan=2)

def add_raamat():
    raamat_andmed_entry = tk.Entry(root)
    raamat_andmed_entry.focus_set()
    raamat_andmed_frame = tk.Toplevel(root)
    raamat_andmed_frame.title("Lisa raamat")
    tk.Label(raamat_andmed_frame, text="Pealkiri:").grid(row=1, column=0)
    pealkiri_entry = tk.Entry(raamat_andmed_frame)
    pealkiri_entry.grid(row=1, column=1)
    tk.Label(raamat_andmed_frame, text="Väljaandmise kuupäev:").grid(row=2, column=0)
    väljaandmise_kuupäev_entry = tk.Entry(raamat_andmed_frame)
    väljaandmise_kuupäev_entry.grid(row=2, column=1)
    tk.Label(raamat_andmed_frame, text="Autor:").grid(row=3, column=0)
    autor_andmed = execute_read_query(connection, "SELECT autor_id, autor_nimi FROM Autorid")
    autor_ids = [row[0] for row in autor_andmed]
    autor_names = [row[1] for row in autor_andmed]
    valitud_autor_id = tk.StringVar()
    autor_id_combobox = ttk.Combobox(raamat_andmed_frame, textvariable=valitud_autor_id, values=autor_ids)
    autor_id_combobox['values'] = autor_names 
    autor_id_combobox.grid(row=3, column=1)
    tk.Label(raamat_andmed_frame, text="Žanr:").grid(row=4, column=0)
    zanr_amded = execute_read_query(connection, "SELECT žanr_id, žanri_nimi FROM Žanrid")
    zanr_ids = [row[0] for row in zanr_amded]
    zanr_names = [row[1] for row in zanr_amded]
    valitud_zanr_id = tk.StringVar()
    zanr_id_combobox = ttk.Combobox(raamat_andmed_frame, textvariable=valitud_zanr_id, values=zanr_ids)
    zanr_id_combobox['values'] = zanr_names
    zanr_id_combobox.grid(row=4, column=1)
    
    def add_raamat_andmebaasi():
        raamat_andmed = (pealkiri_entry.get(), väljaandmise_kuupäev_entry.get(), 
                         valitud_autor_id.get(), valitud_zanr_id.get())
        add_raamat_query(connection, raamat_andmed)
        raamat_andmed_frame.destroy()
    
    add_btn = tk.Button(raamat_andmed_frame, text="Lisa raamat", command=add_raamat_andmebaasi)
    add_btn.grid(row=5, column=0, columnspan=2)


def delete_raamat_pealkirja_järgi():
    uus_window = tk.Toplevel(root)
    uus_window.title("Kustuta Raamat pealkirja järgi")

    juhendamise = tk.Label(uus_window, text="Sisestage kustutamiseks raamatu pealkiri:")
    juhendamise.pack(pady=10)

    global pealkiri_entry  
    pealkiri_entry = tk.Entry(uus_window)
    pealkiri_entry.pack(pady=10)

    def kinnitada_kustutamist():
        pealkiri = pealkiri_entry.get()
        delete_raamat_pealkiri(connection, pealkiri)
        uus_window.destroy()  
    kinnitusnupp = tk.Button(uus_window, text="Kinnita kustutamine", command=kinnitada_kustutamist)
    kinnitusnupp.pack(pady=10)
    
def delete_žanri_nime_järgi():
    uus_window = tk.Toplevel(root)
    uus_window.title("Žanri kustutamine nime järgi")

    juhendamise = tk.Label(uus_window, text="Sisesta kustutamiseks žanrinimi:")
    juhendamise.pack(pady=10)

    global zanr_nimi_entry
    zanr_nimi_entry = tk.Entry(uus_window)
    zanr_nimi_entry.pack(pady=10)

    def kinnitada_kustutamist():
        zanr_nimi = zanr_nimi_entry.get()
        delete_genre_by_name_query(connection, zanr_nimi)
        uus_window.destroy()

    kinnitusnupp = tk.Button(uus_window, text="Kinnita kustutamine", command=kinnitada_kustutamist)
    kinnitusnupp.pack(pady=10)
    

def delete_autor_nime_järgi():
    uus_window = tk.Toplevel(root)
    uus_window.title("Autori kustutamine nime järgi")

    juhendamise = tk.Label(uus_window, text="Sisestage kustutamiseks autori nimi:")
    juhendamise.pack(pady=10)

    global autor_nimi_entry 
    autor_nimi_entry = tk.Entry(uus_window)
    autor_nimi_entry.pack(pady=10)

    def kinnitada_kustutamist():
        autor_nimi = autor_nimi_entry.get()
        delete_autor_by_name(connection, autor_nimi)
        uus_window.destroy()

    kinnitusnupp = tk.Button(uus_window, text="Kinnita kustutamine", command=kinnitada_kustutamist)
    kinnitusnupp.pack(pady=10)



def table_autorid(conn):
    window_autorid = tk.Toplevel() 
    window_autorid.title("Autorite tabel") 
    tree = ttk.Treeview(window_autorid, column=("autor_id", "autor_nimi", "sünnikuupäev"), show="headings")
    tree.column("autor_id", anchor=CENTER)
    tree.heading("autor_id", text="autor_id")
    tree.column("autor_nimi", anchor=CENTER)
    tree.heading("autor_nimi", text="autor_nimi")
    tree.column("sünnikuupäev", anchor=CENTER)
    tree.heading("sünnikuupäev", text="sünnikuupäev")
    try:
        read = execute_read_query(conn, "SELECT * FROM Autorid")
        for row in read:
            tree.insert("", END, values=row)    
    except Exception as e:
        print(f"Viga tabelis autorid: {e}")
    tree.pack() 
    window_autorid.mainloop()
    
def näita_autorid_tabelit():
    table_autorid(connection)
    
def table_zanr(conn):
    window_zanr = tk.Toplevel() 
    window_zanr.title("Žanrite tabel") 
    tree = ttk.Treeview(window_zanr, column=("žanr_id", "žanri_nimi"), show="headings")
    tree.column("žanr_id", anchor=CENTER)
    tree.heading("žanr_id", text="žanr_id")
    tree.column("žanri_nimi", anchor=CENTER)
    tree.heading("žanri_nimi", text="žanri_nimi")
    try:
        read = execute_read_query(conn, "SELECT * FROM Žanrid")
        for row in read:
            tree.insert("", END, values=row)    
    except Exception as e:
        print(f"Viga tabelis zanrid: {e}") 
    tree.pack()
    window_zanr.mainloop()

def näita_zanri_tabelit():
    table_zanr(connection)


def table_raamatud(conn): 
    window_raamatud = tk.Toplevel() 
    window_raamatud.title("Raamatute tabel") 
    tree = ttk.Treeview(window_raamatud, column=("raamat_id", "pealkiri", "väljaandmise_kuupäev", "autor_nimi", "žanri_nimi"), show="headings")
    tree.column("raamat_id", anchor=CENTER)
    tree.heading("raamat_id", text="raamat_id")
    tree.column("pealkiri", anchor=CENTER)
    tree.heading("pealkiri", text="pealkiri") 
    tree.column("väljaandmise_kuupäev", anchor=CENTER)
    tree.heading("väljaandmise_kuupäev", text="väljaandmise_kuupäev") 
    tree.column("autor_nimi", anchor=CENTER)
    tree.heading("autor_nimi", text="autor_nimi") 
    tree.column("žanri_nimi", anchor=CENTER)
    tree.heading("žanri_nimi", text="žanri_nimi")
    try:
        read = execute_read_query(conn, "SELECT r.raamat_id, r.pealkiri, r.väljaandmise_kuupäev, a.autor_nimi, z.žanri_nimi FROM Raamatud r INNER JOIN Autorid a ON r.autor_id = a.autor_id INNER JOIN Žanrid z ON r.žanr_id = z.žanr_id;")
        for row in read:
            tree.insert("", END, values=row)    
    except Exception as e:
        print(f"Viga raamatu tabelis: {e}") 
    tree.pack()
    window_raamatud.mainloop()

    
def näita_raamatud_tabelit():
    table_raamatud(connection)


def delete_table_clicked():
    tabel_nimi = tabel_nimi_entry.get()
    query = f"DROP TABLE IF EXISTS {tabel_nimi}"
    delete_tabel(connection, query)
    window.destroy()

def kustuta_tabeli_liides():
    global window
    window = tk.Toplevel(root)
    window.title("Kustuta Tabel")

    tabel_nimi_label = tk.Label(window, text="Tabeli nimi:")
    tabel_nimi_label.pack(pady=10)

    global tabel_nimi_entry
    tabel_nimi_entry = tk.Entry(window)
    tabel_nimi_entry.pack(pady=5)

    delete_button = tk.Button(window, text="Kustuta", command=delete_table_clicked)
    delete_button.pack(pady=5)


from tkinter import messagebox

def create_valitud_tabel():
    cursor = connection.cursor()
    valitud_tabel = table_combobox.get()
    if valitud_tabel == "Autorid":
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Autorid (
                autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                autor_nimi TEXT NOT NULL,
                sünnikuupäev DATE NOT NULL
            )
        """)
    elif valitud_tabel == "Žanrid":
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Žanrid (
                žanr_id INTEGER PRIMARY KEY AUTOINCREMENT,
                žanri_nimi TEXT NOT NULL
            )
        """)
    elif valitud_tabel == "Raamatud":
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Raamatud (
                raamat_id INTEGER PRIMARY KEY AUTOINCREMENT,
                pealkiri TEXT NOT NULL,
                väljaandmise_kuupäev DATE NOT NULL,
                autor_id INTEGER,
                žanr_id INTEGER,
                FOREIGN KEY(autor_id) REFERENCES Autorid(autor_id),
                FOREIGN KEY(žanr_id) REFERENCES Žanrid(žanr_id)
            )
        """)
    else:
        print("Vigane valik.")
    
    connection.commit()
    messagebox.showinfo("Edu", f"Tabel '{valitud_tabel}' on edukalt loodud")

def insert_initial_data():
    valitud_tabel = algsed_andmed_combobox.get()
    alg_andmed_päringud = {
        "Autorid": [
            "INSERT INTO Autorid(autor_nimi, sünnikuupäev) VALUES ('J.K. Rowling', '1965-07-31')",
            "INSERT INTO Autorid VALUES ('George R.R. Martin', '1948-09-20')"
        ],
        "Žanrid": [
            "INSERT INTO Žanrid VALUES ('Fantaasia')",
            "INSERT INTO Žanrid VALUES ('Sci-Fi')"
        ],
        "Raamatud": [
            "INSERT INTO Raamatud VALUES ('Harry Potter ja filosoofi kivi', '1997-06-26', 1, 1)",
            "INSERT INTO Raamatud VALUES ('Troonide mäng', '1996-08-01', 2, 2)"
        ]
    }
    if valitud_tabel in alg_andmed_päringud:
        for query in alg_andmed_päringud[valitud_tabel]:
            execute_query(connection, query)
        messagebox.showinfo("Edu", f"Esialgsed andmed sisestati {valitud_tabel} tabelisse edukalt")
    else:
        messagebox.showerror("Viga", "Kehtetu tabeli nimi")

root = tk.Tk()
root.title("Raamatukataloog")

######################### show

näidata_andme_frame = tk.Frame(root)
näidata_andme_frame.pack(pady=10)


näidata_autori_btn = tk.Button(näidata_andme_frame, text="Näita Autorite tabelit", command=näita_autorid_tabelit)
näidata_autori_btn.pack(side=tk.LEFT, padx=5)

zanr_table_btn = tk.Button(näidata_andme_frame, text="Näita žanrite tabelit", command=näita_zanri_tabelit)
zanr_table_btn.pack(side=tk.LEFT, padx=5)

raamatud_table_btn = tk.Button(näidata_andme_frame, text="Näita raamatute tabelit", command=näita_raamatud_tabelit)
raamatud_table_btn.pack(side=tk.LEFT, padx=5)
############################################ delete

add_andmed_frame = tk.Frame(root)
add_andmed_frame.pack(pady=10)

delete_autor_button = tk.Button(add_andmed_frame, text="Autori kustutamine nime järgi", command=delete_autor_nime_järgi)
delete_autor_button.pack(side=tk.LEFT, padx=5)

delete_zanr_button = tk.Button(add_andmed_frame, text="Žanri kustutamine nime järgi", command=delete_žanri_nime_järgi)
delete_zanr_button.pack(side=tk.LEFT, padx=5)

delete_pealkiri_button = tk.Button(add_andmed_frame, text="Kustuta Raamat pealkirja järgi", command=delete_raamat_pealkirja_järgi)
delete_pealkiri_button.pack(side=tk.LEFT, padx=5)
################################### update

update_frame = tk.Frame(root)
update_frame.pack(pady=10)

autor_nimi = [row[0] for row in execute_read_query(connection, "SELECT autor_nimi FROM Autorid")]
näidata_andme_frame = tk.Frame(root)
näidata_andme_frame.pack(pady=10)

autor_nimi_label = tk.Label(näidata_andme_frame, text="Valige Autori nimi:")
autor_nimi_label.pack(side=tk.LEFT, padx=5)

valitud_autor_nimi = tk.StringVar()
autor_nimi_combobox = ttk.Combobox(näidata_andme_frame, textvariable=valitud_autor_nimi, values=autor_nimi)
autor_nimi_combobox.pack(side=tk.LEFT, padx=5)

uus_nimi_label = tk.Label(näidata_andme_frame, text="Uus nimi:")
uus_nimi_label.pack(side=tk.LEFT, padx=5)
uus_nimi_entry = tk.Entry(näidata_andme_frame)
uus_nimi_entry.pack(side=tk.LEFT, padx=5)

update_autor_button = tk.Button(näidata_andme_frame, text="Uuenda autorinime", command=update_autor_nimi2)
update_autor_button.pack(side=tk.LEFT, padx=5)

zanr_nimi = [row[0] for row in execute_read_query(connection, "SELECT žanri_nimi FROM Žanrid")]
update_zanr_frame = tk.Frame(root)
update_zanr_frame.pack(pady=10)

zanr_nimi_label = tk.Label(update_zanr_frame, text="Valige žanri nimi:")
zanr_nimi_label.pack(side=tk.LEFT, padx=5)

valitud_zanr_nimi = tk.StringVar()
zanr_nimi_combobox = ttk.Combobox(update_zanr_frame, textvariable=valitud_zanr_nimi, values=zanr_nimi)
zanr_nimi_combobox.pack(side=tk.LEFT, padx=5)

uus_zanr_nimi_label = tk.Label(update_zanr_frame, text="Uue žanri nimi:")
uus_zanr_nimi_label.pack(side=tk.LEFT, padx=5)
uus_zanr_nimi_entry = tk.Entry(update_zanr_frame)
uus_zanr_nimi_entry.pack(side=tk.LEFT, padx=5)

update_zanr_button = tk.Button(update_zanr_frame, text="Uuenda žanri nime", command=update_zanr_nimi2)
update_zanr_button.pack(side=tk.LEFT, padx=5)

raamat_pealkiris = [row[0] for row in execute_read_query(connection, "SELECT pealkiri FROM Raamatud")]
update_raamat_frame = tk.Frame(root)
update_raamat_frame.pack(pady=10)

raamat_pealkiri_label = tk.Label(update_raamat_frame, text="Vali raamatu pealkiri:")
raamat_pealkiri_label.pack(side=tk.LEFT, padx=5)

valitud_raamat_pealkiri = tk.StringVar()
raamat_pealkiri_combobox = ttk.Combobox(update_raamat_frame, textvariable=valitud_raamat_pealkiri, values=raamat_pealkiris)
raamat_pealkiri_combobox.pack(side=tk.LEFT, padx=5)

uus_pealkiri_label = tk.Label(update_raamat_frame, text="Uus pealkiri:")
uus_pealkiri_label.pack(side=tk.LEFT, padx=5)
uus_pealkiri_entry = tk.Entry(update_raamat_frame)
uus_pealkiri_entry.pack(side=tk.LEFT, padx=5)

update_raamat_button = tk.Button(update_raamat_frame, text="Uuenda raamatu pealkirja", command=update_raamat_pealkiri2)
update_raamat_button.pack(side=tk.LEFT, padx=5)
########################## add

add_frame = tk.Frame(root)
add_frame.pack(pady=10)

add_autor_btn = tk.Button(add_frame, text="Lisa autor", command=add_autor)
add_autor_btn.pack(side=tk.LEFT, padx=5)

add_zanr_btn = tk.Button(add_frame, text="Lisa žanr", command=add_zanr)
add_zanr_btn.pack(side=tk.LEFT, padx=5)

add_raamat_btn = tk.Button(add_frame, text="Lisa raamat", command=add_raamat)
add_raamat_btn.pack(side=tk.LEFT, padx=5)

delete_table_btn = tk.Button(root, text="Kustuta tabel", command=kustuta_tabeli_liides)
delete_table_btn.pack(pady=10)
####################### create

table_combobox = ttk.Combobox(root, width=30, height=10)
table_combobox['values'] = ("Autorid", "Žanrid", "Raamatud")
table_combobox.pack(side=tk.LEFT, padx=(10, 5)) 

create_button = tk.Button(root, text="Tabeli loomine", command=create_valitud_tabel)
create_button.pack(side=tk.LEFT, pady=10, padx=(5, 10))

############################ add andmed tabelis

algsed_andmed_combobox = ttk.Combobox(root, width=30, height=10)
algsed_andmed_combobox['values'] = ("Autorid", "Žanrid", "Raamatud")
algsed_andmed_combobox.pack(side=tk.LEFT, padx=(10, 5))

insert_initial_data_button = tk.Button(root, text="Lisage algandmed", command=insert_initial_data)
insert_initial_data_button.pack(side=tk.LEFT, padx=(5, 10))



root.mainloop()
