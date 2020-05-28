import tkinter as tk
from tkinter import messagebox


class DataScreen(tk.Frame):

    def back(self):
        self.controller.show_frame("FirstScreen")

    def __init__(self, parent, controller, pages):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.pages = pages

        self.entryLabel = tk.Label(self, text='Entry')
        self.subjectCodeLabel = tk.Label(self, text='Subject Code')
        self.scriptNoLabel = tk.Label(self, text='Script No.')
        self.marksRegLabel = tk.Label(self, text='Marks/Reg No.')

        validation = self._register(self.only_numeric_input)

        self.entry = "ENTRY_VALUE"
        self.subjectCode = "SUBJECT_CODE"
        self.scriptNo = "SCRIPT_NO"

        self.entryVal = tk.Label(self, text=self.entry)
        self.subjectCodeVal = tk.Label(self, text=self.subjectCode)
        self.scriptNoVal = tk.Label(self, text=self.scriptNo)
        self.marksRegVal = tk.Entry(self, validate="key",
                                    validatecommand=(validation, '%S'))

        self.enterData = tk.Button(self, text="Enter Data",
                                   command=self.finalValidation)
        self.back = tk.Button(self, text="Back", command=self.back)

        self.entryLabel.place(x=200, y=100)
        self.subjectCodeLabel.place(x=200, y=200)
        self.scriptNoLabel.place(x=200, y=300)
        self.marksRegLabel.place(x=200, y=400)

        self.entryVal.place(x=500, y=100)
        self.subjectCodeVal.place(x=500, y=200)
        self.scriptNoVal.place(x=500, y=300)
        self.marksRegVal.place(x=500, y=400)

        self.back.place(x=200, y=600)
        self.enterData.place(x=500, y=600)

    def only_numeric_input(self, e):
        return bool(e.isdigit())

    def finalValidation(self):
        marks = self.t4.get()
        if(len(marks) == 0):
            messagebox.showerror("Error", "Marks Cannot be NULL")
        elif (int(marks) > 100):
            messagebox.showerror("Error", "Check Again")
        else:
            messagebox._show("Inkempo Macha", "Kottav Chance")
