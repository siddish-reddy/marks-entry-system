import tkinter as tk
import tkinter.messagebox


class FirstScreen:
    def __init__(self, root):
        # creating labels
        subject_code_label = tk.Label(root, text="Subject Code")
        title_label = tk.Label(root, text="Subject Title")
        script_code_label = tk.Label(root, text="Script Code")
        starting_script_code_label = tk.Label(
            root, text="Script Starting Code")
        no_of_scripts_label = tk.Label(root, text="No. of Scripts")
        operator_label = tk.Label(root, text="Data Operator Name")
        entry_label = tk.Label(root, text="Choose Entry")

        validation = root.register(self.only_numeric_input)

        # creating entries
        subject_code_entry = tk.Entry(root)
        title_entry = tk.Entry(root)
        script_code_entry = tk.Entry(root, validate="key",
                                     validatecommand=(validation, '%S'))
        starting_script_code_entry = tk.Entry(root, validate="key",
                                              validatecommand=(validation, '%S'))
        no_of_scripts_entry = tk.Entry(root, validate="key",
                                       validatecommand=(validation, '%S'))
        operator_entry = tk.Entry(root)
        entry_label = tk.Entry(root)

        def submit():
            subject_code = subject_code_entry.get()
            title = title_entry.get()
            script_code = script_code_entry.get()
            starting_script_code = starting_script_code_entry.get()
            no_of_scripts = no_of_scripts_entry.get()
            operator = operator_entry.get()

            if(subject_code == '' and title == '' and script_code == '' and starting_script_code == '' and no_of_scripts == '' and operator == ''):
                tk.messagebox.showerror('ERROR', 'PLEASE ENTER THE VALUES')

            else:
                self.clear()
                # Order
                data_object = [
                    subject_code,
                    title,
                    script_code,
                    starting_script_code,
                    no_of_scripts,
                    operator
                ]

                dataScreen = SecondScreen(window, data_object)

        continue_button = tk.Button(root, text="Continue", command=submit)

        # Rendering all elements
        subject_code_label.place(x=200, y=100)
        title_label.place(x=200, y=150)
        script_code_label.place(x=200, y=200)
        starting_script_code_label.place(x=200, y=250)
        no_of_scripts_label.place(x=200, y=300)
        operator_label.place(x=200, y=350)

        subject_code_entry.place(x=500, y=100)
        title_entry.place(x=500, y=150)
        script_code_entry.place(x=500, y=200)
        starting_script_code_entry.place(x=500, y=250)
        no_of_scripts_entry.place(x=500, y=300)
        operator_entry.place(x=500, y=350)
        continue_button.place(x=200, y=400)

    def only_numeric_input(self, e):
        if e.isdigit():
            return True
        elif e == "":
            return True
        else:
            return False

    def all_children(self, window):
        _list = window.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())

        return _list

    def clear(self):
        widget_list = self.all_children(window)
        for item in widget_list:
            item.destroy()


class SecondScreen:
    def __init__(self, root, data):
        subject_code_label = tk.Label(root, text="Subject Code")
        script_code_label = tk.Label(root, text="Script Code")
        entry_label = tk.Label(root, text="Entry")
        marks_label = tk.Label(root, text="Marks")

        validation = root.register(self.only_numeric_input)

        subject_code_value = tk.Label(root, text=data[0])
        script_code_value = tk.Label(root, text=data[2])
        entry_value = tk.Label(root, text=data[2])
        marks_reg_value = tk.Entry(root, validate="key",
                                   validatecommand=(validation, '%S'))

        def submit():
            # Insert Data to DataBase
            script_code = int(data[2]) + 1
            data[2] = script_code
            script_code_value.config(text=script_code)

        enter_button = tk.Button(root, text="Enter", command=submit)

        # render all elements
        subject_code_label.place(x=200, y=100)
        script_code_label.place(x=200, y=150)
        entry_label.place(x=200, y=200)
        marks_label.place(x=200, y=250)

        subject_code_value.place(x=500, y=100)
        script_code_value.place(x=500, y=150)
        entry_value.place(x=500, y=200)
        marks_reg_value.place(x=500, y=250)

        enter_button.place(x=200, y=300)

    def only_numeric_input(self, e):
        if e.isdigit():
            return True
        elif e == "":
            return True
        else:
            return False


if __name__ == "__main__":
    window = tk.Tk()
    first_screen = FirstScreen(window)
    window.geometry("1366x760+10+10")
    window.title("")
    window.mainloop()
