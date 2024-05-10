from tkinter import ttk
import tkinter as tk
from tkinter.constants import CENTER, END
from tkinter import messagebox
from def_raamat import *


def update_autor_nimi2():
    autor_id = valitud_autor_id.get()
    uus_nimi = uus_nimi_entry.get()
    update_autor_nimi(connection, (uus_nimi, autor_id))
    uus_nimi_entry.delete(0, END)

def update_zanr_nimi2():
    genre_id = valitud_zanr_id.get()
    uus_nimi = uus_zanr_nimi_entry.get()
    update_zanr_nimi(connection, (uus_nimi, genre_id))
    uus_zanr_nimi_entry.delete(0, END)

def update_raamat_pealkiri2():
    book_id = valitud_raamat_id.get()
    uus_pealkiri = uus_pealkiri_entry.get()
    update_raamat_pealkiri(connection, (uus_pealkiri, book_id))
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
    tk.Label(raamat_andmed_frame, text="Autor ID:").grid(row=3, column=0)
    autor_id_entry = tk.Entry(raamat_andmed_frame)
    autor_id_entry.grid(row=3, column=1)
    tk.Label(raamat_andmed_frame, text="Žanr ID:").grid(row=4, column=0)
    zanr_id_entry = tk.Entry(raamat_andmed_frame)
    zanr_id_entry.grid(row=4, column=1)
    
    def add_book_to_database():
        raamat_andmed = (pealkiri_entry.get(), väljaandmise_kuupäev_entry.get(), 
                     autor_id_entry.get(), zanr_id_entry.get())
        add_raamat_query(connection, raamat_andmed)
        raamat_andmed_frame.destroy()
    
    add_btn = tk.Button(raamat_andmed_frame, text="Lisa raamat", command=add_book_to_database)
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

def näita_all_andmeid():
    allData = """
    SELECT r.pealkiri, a.autor_nimi, z.žanri_nimi
    FROM Raamatud r
    INNER JOIN Autorid a ON r.autor_id = a.autor_id
    INNER JOIN Žanrid z ON r.žanr_id = z.žanr_id;
    """
    result = execute_read_query(connection, allData)
    if result:
        andmed_window = tk.Toplevel(root)
        andmed_window.title("Kõik andmed")
        
        text_widget = tk.Text(andmed_window, width=40, height=10)
        text_widget.pack()
        
        for row in result:
            text_widget.insert(tk.END, f"{row}\n")
    else:
        print("Andmeid ei leitud")

def table_autorid(conn):
    window_autorid = tk.Tk() 
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
    window_zanr = tk.Tk() 
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
    window_raamatud = tk.Tk() 
    window_raamatud.title("Raamatute tabel") 
    tree = ttk.Treeview(window_raamatud, column=("raamat_id", "pealkiri", "väljaandmise_kuupäev", "autor_id", "zanr_id"), show="headings")
    tree.column("raamat_id", anchor=CENTER)
    tree.heading("raamat_id", text="raamat_id")
    tree.column("pealkiri", anchor=CENTER)
    tree.heading("pealkiri", text="pealkiri") 
    tree.column("väljaandmise_kuupäev", anchor=CENTER)
    tree.heading("väljaandmise_kuupäev", text="väljaandmise_kuupäev") 
    tree.column("autor_id", anchor=CENTER)
    tree.heading("autor_id", text="autor_id") 
    tree.column("zanr_id", anchor=CENTER)
    tree.heading("zanr_id", text="zanr_id") 
    try:
        read = execute_read_query(conn, "SELECT * FROM Raamatud ")
        for row in read:
            tree.insert("", END, values=row)    
    except Exception as e:
        print(f"Viga raamatu tabelis: {e}") 
    tree.pack()
    window_raamatud.mainloop()
    
def näita_raamatud_tabelit():
    table_raamatud(connection)



root = tk.Tk()
root.title("Raamatukataloog")


näidata_andme_frame = tk.Frame(root)
näidata_andme_frame.pack(pady=10)

näidata_andme_btn = tk.Button(näidata_andme_frame, text="Näita kõiki andmeid", command=näita_all_andmeid)
näidata_andme_btn.pack(side=tk.LEFT, padx=5)

näidata_autori_btn = tk.Button(näidata_andme_frame, text="Näita Autorite tabelit", command=näita_autorid_tabelit)
näidata_autori_btn.pack(side=tk.LEFT, padx=5)

zanr_table_btn = tk.Button(näidata_andme_frame, text="Näita žanrite tabelit", command=näita_zanri_tabelit)
zanr_table_btn.pack(side=tk.LEFT, padx=5)

raamatud_table_btn = tk.Button(näidata_andme_frame, text="Näita raamatute tabelit", command=näita_raamatud_tabelit)
raamatud_table_btn.pack(side=tk.LEFT, padx=5)


delete_frame = tk.Frame(root)
delete_frame.pack(pady=10)

delete_autor_button = tk.Button(delete_frame, text="Autori kustutamine nime järgi", command=delete_autor_nime_järgi)
delete_autor_button.pack(side=tk.LEFT, padx=5)

delete_zanr_button = tk.Button(delete_frame, text="Žanri kustutamine nime järgi", command=delete_žanri_nime_järgi)
delete_zanr_button.pack(side=tk.LEFT, padx=5)

delete_pealkiri_button = tk.Button(delete_frame, text="Kustuta Raamat pealkirja järgi", command=delete_raamat_pealkirja_järgi)
delete_pealkiri_button.pack(side=tk.LEFT, padx=5)


update_frame = tk.Frame(root)
update_frame.pack(pady=10)

autor_ids = [row[0] for row in execute_read_query(connection, "SELECT autor_id FROM Autorid")]
näidata_andme_frame = tk.Frame(root)
näidata_andme_frame.pack(pady=10)

autor_id_label = tk.Label(näidata_andme_frame, text="Valige Autori ID:")
autor_id_label.pack(side=tk.LEFT, padx=5)

valitud_autor_id = tk.StringVar()
autor_id_combobox = ttk.Combobox(näidata_andme_frame, textvariable=valitud_autor_id, values=autor_ids)
autor_id_combobox.pack(side=tk.LEFT, padx=5)

uus_nimi_label = tk.Label(näidata_andme_frame, text="Uus nimi:")
uus_nimi_label.pack(side=tk.LEFT, padx=5)
uus_nimi_entry = tk.Entry(näidata_andme_frame)
uus_nimi_entry.pack(side=tk.LEFT, padx=5)

update_autor_button = tk.Button(näidata_andme_frame, text="Uuenda autorinime", command=update_autor_nimi2)
update_autor_button.pack(side=tk.LEFT, padx=5)

zanr_ids = [row[0] for row in execute_read_query(connection, "SELECT žanr_id FROM Žanrid")]
update_zanr_frame = tk.Frame(root)
update_zanr_frame.pack(pady=10)

zanr_id_label = tk.Label(update_zanr_frame, text="Valige žanri ID:")
zanr_id_label.pack(side=tk.LEFT, padx=5)

valitud_zanr_id = tk.StringVar()
zanr_id_combobox = ttk.Combobox(update_zanr_frame, textvariable=valitud_zanr_id, values=zanr_ids)
zanr_id_combobox.pack(side=tk.LEFT, padx=5)

uus_zanr_nimi_label = tk.Label(update_zanr_frame, text="Uue žanri nimi:")
uus_zanr_nimi_label.pack(side=tk.LEFT, padx=5)
uus_zanr_nimi_entry = tk.Entry(update_zanr_frame)
uus_zanr_nimi_entry.pack(side=tk.LEFT, padx=5)

update_zanr_button = tk.Button(update_zanr_frame, text="Uuenda žanri nime", command=update_zanr_nimi2)
update_zanr_button.pack(side=tk.LEFT, padx=5)

raamat_ids = [row[0] for row in execute_read_query(connection, "SELECT raamat_id FROM Raamatud")]
update_raamat_frame = tk.Frame(root)
update_raamat_frame.pack(pady=10)

raamat_id_label = tk.Label(update_raamat_frame, text="Vali raamatu ID:")
raamat_id_label.pack(side=tk.LEFT, padx=5)

valitud_raamat_id = tk.StringVar()
raamat_id_combobox = ttk.Combobox(update_raamat_frame, textvariable=valitud_raamat_id, values=raamat_ids)
raamat_id_combobox.pack(side=tk.LEFT, padx=5)

uus_pealkiri_label = tk.Label(update_raamat_frame, text="Uus pealkiri:")
uus_pealkiri_label.pack(side=tk.LEFT, padx=5)
uus_pealkiri_entry = tk.Entry(update_raamat_frame)
uus_pealkiri_entry.pack(side=tk.LEFT, padx=5)

update_raamat_button = tk.Button(update_raamat_frame, text="Uuenda raamatu pealkirja", command=update_raamat_pealkiri2)
update_raamat_button.pack(side=tk.LEFT, padx=5)

add_frame = tk.Frame(root)
add_frame.pack(pady=10)

add_autor_btn = tk.Button(add_frame, text="Lisa autor", command=add_autor)
add_autor_btn.pack(side=tk.LEFT, padx=5)

add_zanr_btn = tk.Button(add_frame, text="Lisa žanr", command=add_zanr)
add_zanr_btn.pack(side=tk.LEFT, padx=5)

add_raamat_btn = tk.Button(add_frame, text="Lisa raamat", command=add_raamat)
add_raamat_btn.pack(side=tk.LEFT, padx=5)


root.mainloop()
