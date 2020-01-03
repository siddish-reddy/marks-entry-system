import tkinter as tk
import tkinter.messagebox
window = tk.Tk()

window.title("Data entry registration")

subject_code = tk.StringVar()
title = tk.StringVar()
script_code = tk.IntVar()
script_start_no = tk.IntVar()
no_of_scripts = tk.IntVar()
data_operator_name = tk.StringVar()
entry = tk.IntVar()

#heading = tk.Label("Data entry registration")
subject_code_label = tk.Label(window, text="Subject Code:")
title_label = tk.Label(window, text="Subject Title:")
script_code_label = tk.Label(window, text="Script Code:")
script_start_no_label = tk.Label(window, text="Script Start no.:")
no_of_scripts_label = tk.Label(window, text="Number of scripts:")
data_operator_name_label = tk.Label(window, text="Data Operator Name:")

subject_code_input = tk.Entry(window)
title_input = tk.Entry(window)
script_code_input = tk.Entry(window)
script_start_no_input = tk.Entry(window)
no_of_scripts_input = tk.Entry(window)
data_operator_name_input = tk.Entry(window)
entry_1_input = tk.Radiobutton(window, text='Entry 1', value=1, variable=entry)
entry_2_input = tk.Radiobutton(window, text='Entry 2', value=2, variable=entry)
entry_1_input.select()
def submit():
    subject = subject_code_input.get()
    title = title_input.get()
    script = script_code_input.get()
    script_start_no = script_start_no_input.get()
    no_of_scripts = no_of_scripts_input.get()
    data_operator_name = data_operator_name_input.get()

    #validation logics:
    validation_error = ''
    valid = True

    if subject=='' or title=='':
        validation_error += "~ Subject or title should not be empty\n\n"
        valid = False
    
    if len(subject)>20 or len(subject)<5:
        validation_error +='~ Subject code of invalid length \n\n'
        valid = False
        
    if len(title)>30 or len(subject)<5:
        validation_error +='~ Subject title of invalid length \n\n'
        valid = False
    
    if not no_of_scripts.isdigit():
        validation_error +='~ Number of scripts should be a number\n\n'
        valid = False
    else:
        no_of_scripts = int(no_of_scripts)
        if no_of_scripts<=0:
            validation_error +='~ Number of scripts should be a positive\n\n'
            valid = False

    if len(data_operator_name)<5:
        validation_error +='~ Please enter valid name\n\n'
        valid = False
    
    if not valid:
        tk.messagebox.showerror('error',validation_error)
    
        
    
submit_button = tk.Button(window, text="Continue", command=submit)

subject_code_label.grid(row=0, column=0);
title_label.grid(row=1, column=0)
script_code_label.grid(row=2, column=0)
script_start_no_label.grid(row=3, column=0)
no_of_scripts_label.grid(row=4, column=0)
data_operator_name_label.grid(row=5, column=0)

subject_code_input.grid(row=0, column=1, padx=30, pady=5);
title_input.grid(row=1, column=1, padx=30, pady=5);
script_code_input.grid(row=2, column=1, padx=30, pady=5);
script_start_no_input.grid(row=3, column=1, padx=30, pady=5);
no_of_scripts_input.grid(row=4, column=1, padx=30, pady=5);
data_operator_name_input.grid(row=5, column=1, padx=30, pady=5);
entry_1_input.grid(row=6, column=0, padx=15, pady=5);
entry_2_input.grid(row=6, column=1, padx=15, pady=5);

submit_button.grid(row=7, column=1, padx=50, pady=10)
window.mainloop()
