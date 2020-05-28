import tkinter as tk
from tkinter import messagebox


class FirstScreen(tk.Frame):
    def __init__(self, parent, controller, pages):

        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.pages = pages

        self.subject_code = tk.StringVar()
        self.title = tk.StringVar()
        self.script_code = tk.IntVar()
        self.script_start_no = tk.IntVar()
        self.no_of_scripts = tk.IntVar()
        self.data_operator_name = tk.StringVar()
        self.entry = tk.IntVar()

        self.subject_code_label = tk.Label(self, text="Subject Code:")
        self.title_label = tk.Label(self, text="Subject Title:")
        self.script_code_label = tk.Label(self, text="Script Code:")
        self.script_start_no_label = tk.Label(self, text="Script Start no.:")
        self.no_of_scripts_label = tk.Label(self, text="Number of scripts:")
        self.data_operator_name_label = tk.Label(self,
                                                 text="Data Operator Name:")
        self.submit_button = tk.Button(self,
                                       text="Continue", command=self.submit)

        validation = self._register(self.only_numeric_input)

        self.subject_code_input = tk.Entry(self)
        self.title_input = tk.Entry(self)
        self.script_code_input = tk.Entry(
            self, validate="key",  validatecommand=(validation, '%S'))
        self.script_start_no_input = tk.Entry(
            self, validate="key",  validatecommand=(validation, '%S'))
        self.no_of_scripts_input = tk.Entry(
            self, validate="key",  validatecommand=(validation, '%S'))
        self.data_operator_name_input = tk.Entry(self)
        self.entry_1_input = tk.Radiobutton(
            self, text='Entry 1', value=1, variable=self.entry)
        self.entry_2_input = tk.Radiobutton(
            self, text='Entry 2', value=2, variable=self.entry)

        self.subject_code_label.grid(row=0, column=0)
        self.title_label.grid(row=1, column=0)
        self.script_code_label.grid(row=2, column=0)
        self.script_start_no_label.grid(row=3, column=0)
        self.no_of_scripts_label.grid(row=4, column=0)
        self.data_operator_name_label.grid(row=5, column=0)

        self.subject_code_input.grid(row=0, column=1, padx=30, pady=5)
        self.title_input.grid(row=1, column=1, padx=30, pady=5)
        self.script_code_input.grid(row=2, column=1, padx=30, pady=5)
        self.script_start_no_input.grid(row=3, column=1, padx=30, pady=5)
        self.no_of_scripts_input.grid(row=4, column=1, padx=30, pady=5)
        self.data_operator_name_input.grid(row=5, column=1, padx=30, pady=5)
        self.entry_1_input.grid(row=6, column=0, padx=15, pady=5)
        self.entry_2_input.grid(row=6, column=1, padx=15, pady=5)
        self.submit_button.grid(row=7, column=1, padx=50, pady=10)

    def submit(self):
        subject = self.subject_code_input.get()
        title = self.title_input.get()
        script = self.script_code_input.get()
        script_start_no = self.script_start_no_input.get()
        no_of_scripts = self.no_of_scripts_input.get()
        data_operator_name = self.data_operator_name_input.get()

        # validation logics:
        validation_error = ''
        valid = True

        if subject == '' or title == '' or \
           script == '' or script_start_no == '':
            validation_error += "~ Subject or title should not be empty\n\n"
            valid = False

        if len(subject) > 20 or len(subject) < 5:
            validation_error += '~ Subject code of invalid length \n\n'
            valid = False

        if len(title) > 30 or len(subject) < 5:
            validation_error += '~ Subject title of invalid length \n\n'
            valid = False

        if not no_of_scripts.isdigit():
            validation_error += '~ Number of scripts should be a number\n\n'
            valid = False
        else:
            no_of_scripts = int(no_of_scripts)
            if no_of_scripts <= 0:
                validation_error += '~ Number of scripts\
                                    should be a positive\n\n'
                valid = False

        if len(data_operator_name) < 5:
            validation_error += '~ Please enter valid name\n\n'
            valid = False

        if not valid:
            messagebox.showerror('error', validation_error)
        else:
            self.controller.frames['DataScreen'].entryVal.config(text=self.entry)
            self.controller.frames['DataScreen'].subjectCodeVal.config(text=self.subject_code_input.get())
            self.controller.frames['DataScreen'].scriptNoVal.config(text=self.script_code_input.get())
            self.controller.show_frame("DataScreen")

    def only_numeric_input(self, e):
        return bool(e.isdigit() or not e.isdigit() and e == "")
