from tkinter import *
from  tkinter import ttk


def init(alerts, alert):
    ws = Tk()
    ws.title('TakaLogger')
    ws.geometry('700x300')

    table = ttk.Treeview(ws)
    table.pack()

    table['columns']= ('תאריך', 'שם האתר', 'סוג תקלה')
    table.column("#0", width=0, stretch=NO)
    table.column("תאריך", width=200)
    table.column("שם האתר", width=200)
    table.column("סוג תקלה", width=300)

    table.heading("#0", text="", anchor=CENTER)
    table.heading("תאריך", text="תאריך", anchor=CENTER)
    table.heading("שם האתר", text="שם האתר", anchor=CENTER)
    table.heading("סוג תקלה", text="סוג תקלה", anchor=CENTER)

    for i in range(len(alerts)):
        table.insert(parent='', index='end', text='',
                        values=(alerts[i]["Time"], alerts[i]["Site"], alerts[i]["Error"]))
    # table.insert(parent='', index='end', iid=0, text='',
                  # values=(alert["Time"], alert["Site"], alert["Error"]))

    ws.mainloop()