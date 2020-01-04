import tkinter as tk
from tkinter import messagebox


class DataScreen(tk.Frame):

    def back(self):
        self.destroy()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.l1 = tk.Label(self, text='Entry')
        self.l2 = tk.Label(self, text='Subject Code')
        self.l3 = tk.Label(self, text='Script No.')
        self.l4 = tk.Label(self, text='Marks/Reg No.')

        validation = self._register(self.only_numeric_input)

        self.t1 = tk.Label(self, text='Entry')
        self.t2 = tk.Label(self, text='Subject Code')
        self.t3 = tk.Label(self, text='Something')
        self.t4 = tk.Entry(self, validate="key",
                           validatecommand=(validation, '%S'))

        self.enterData = tk.Button(self, text="Enter Data",
                                   command=self.finalValidation)
        self.back = tk.Button(self, text="Back", command=self.back)

        self.l1.place(x=200, y=100)
        self.l2.place(x=200, y=200)
        self.l3.place(x=200, y=300)
        self.l4.place(x=200, y=400)

        self.t1.place(x=500, y=100)
        self.t2.place(x=500, y=200)
        self.t3.place(x=500, y=300)
        self.t4.place(x=500, y=400)

        self.back.place(x=200, y=600)
        self.enterData.place(x=500, y=600)

    def only_numeric_input(self, e):
        if e.isdigit():
            return True
        elif e == "":
            return False
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
