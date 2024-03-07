from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Calendario")
root.geometry("500x350")
root.config(bg="gray")

cal = Calendar(root, select="day", year=2022, month=11, day=21)
cal.pack(pady=20, fill="both", expand="yes")

def Fecha():
    Label.config(text="Fecha de hoy" + cal.get_date())




root.mainloop()