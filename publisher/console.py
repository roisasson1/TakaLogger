from tkinter import *
from tkinter import ttk


def init(name_of_site, message):
    ws = Tk()
    ws.title("TakaLogger")
    ws.geometry('700x300')
    # Create label
    headline = Label(ws, text=f'ניטור חניון: {name_of_site}')
    headline.config(font=("Courier", 14))
    headline.pack()

    table = ttk.Treeview(ws)
    table.pack()

    table['columns']= ('תאריך', 'מקור', 'סוג תקלה')
    table.column("#0", width=0, stretch=NO)
    table.column("תאריך", width=200)
    table.column("מקור", width=200)
    table.column("סוג תקלה", width=300)

    table.heading("#0", text="", anchor=CENTER)
    table.heading("תאריך", text="תאריך", anchor=CENTER)
    table.heading("מקור", text="מקור", anchor=CENTER)
    table.heading("סוג תקלה", text="סוג תקלה", anchor=CENTER)

    table.insert(parent='', index='end', iid=0, text='',
                  values=(message["Time"], "תוכנה", message["Error"]))

    ws.mainloop()