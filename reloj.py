# Reloj hecho con Python, Tkinter y time
# croquetas
# Más croquetas
# Muchísmas croquetas
# Más que muchísimas croquetas




from tkinter import *
import time
 
class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", font=("Calibri", 20))
        self.label.place(x=50,y=80)
        self.update_clock()
 
    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)
 
root = Tk()
app=App(root)
root.wm_title("Clock")
root.geometry("200x200")
root.resizable(width=False, height=False)
root.after(1000, app.update_clock)
root.mainloop()
