from tkinter import *
from tkinter import messagebox

class DataScreen:

    def close_window(self):
        self.window.destroy()

    def __init__(self, window):
        self.window = window
    
        self.l1 = Label(window, text='Entry')
        self.l2 = Label(window, text='Subject Code')
        self.l3 = Label(window, text='Script No.')
        self.l4 = Label(window, text='Marks/Reg No.')

        validation = self.window.register(self.only_numeric_input)
        
        self.t1 = Label(window, text='Entry')
        self.t2 = Label(window, text='Subject Code')
        self.t3 = Label(window, text='Something')
        self.t4 = Entry(window, validate = "key",  validatecommand=(validation, '%S'))

        self.enterData = Button(window, text="Enter Data", command = self.finalValidation)
        self.quit = Button(window, text="Quit", command=self.close_window)

        self.l1.place(x=200, y=100)
        self.l2.place(x=200, y=200)
        self.l3.place(x=200, y=300)
        self.l4.place(x=200, y=400)

        self.t1.place(x=500, y=100)
        self.t2.place(x=500, y=200)
        self.t3.place(x=500, y=300)
        self.t4.place(x=500, y=400)

        self.quit.place(x=200, y=600)
        self.enterData.place(x=500, y=600)



    def only_numeric_input(self, e):
        if e.isdigit():
            return True
        elif e == "":
            return True
        else:
            return False

    def finalValidation(self):
        marks = self.t4.get()
        if(len(marks) == 0):
            messagebox.showerror("Error", "Marks Cannot be NULL")
        elif (int(marks) > 100):
            messagebox.showerror("Error", "Check Again")
        else:
            messagebox._show("Inkempo Macha", "Kottav Chance")
        




window = Tk()
mywin = DataScreen(window)
window.title('Hello Python')
window.geometry("1366x760+10+10")
window.mainloop()
