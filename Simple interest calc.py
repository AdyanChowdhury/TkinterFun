import tkinter as tk
import tkinter.ttk as ttk

def simple_interest_calculator():
    p = p_var.get()
    r = r_var.get()
    t = t_var.get()
    i = i_var.get()

    if p!= "" and r!="" and t != "" and i == "":
        try:
            i=float(p)*float(r)*float(t)/100
            i_var.set(str(i))
        except:
            print("invalid input")
    elif i!= "" and t!="" and r != "" and p == "": 
        try:
            p= float(i)*100/float(r)*float(t)
            p_var.set(str(p))
        except:
            print("invalid input")
    elif i!= "" and p!="" and r != "" and t == "": 
        try:
            t= float(i)*100/(float(r)*float(p))
            t_var.set(str(t))
        except:
            print("invalid input")
    elif i!= "" and t!="" and p != "" and r == "": 
        try:
            r= float(i)*100/(float(p)*float(t))
            r_var.set(str(r))
        except:
            print("invalid input")
def clear():
    p_var=""
    t_var=""
    i_var=""
    r_var=""
root = tk.Tk()

entry_frame = tk.Frame(root)
entry_frame.grid(row=0, column=0, sticky=tk.W+tk.E)

p_label = ttk.Label(entry_frame, text="P =")
p_label.grid(row=0, column=1, sticky=tk.W)
p_var = tk.StringVar()
p_entry = ttk.Entry(entry_frame, textvariable=p_var)
p_entry.grid(row=0, column=2, sticky=tk.E, pady=10, padx=5)


r_label = ttk.Label(entry_frame, text="R =")
r_label.grid(row=1, column=1, sticky=tk.W)
r_var = tk.StringVar()
r_entry = ttk.Entry(entry_frame, textvariable=r_var)
r_entry.grid(row=1, column=2, sticky=tk.E,pady=10,padx=5)

t_label = ttk.Label(entry_frame, text="T =")
t_label.grid(row=2, column=1, sticky=tk.W)
t_var = tk.StringVar()
t_entry = ttk.Entry(entry_frame, textvariable=t_var)
t_entry.grid(row=2, column=2, sticky=tk.E, pady=10, padx=5)

i_label = ttk.Label(entry_frame, text="I =")
i_label.grid(row=3, column=1, sticky=tk.W)
i_var = tk.StringVar()
i_entry = ttk.Entry(entry_frame, textvariable=i_var)
i_entry.grid(row=3, column=2, sticky=tk.E, pady=10,padx=5)

button_frame =tk.Frame(root)
button_frame.grid(row=1, column=0)

calculate_button=ttk.Button(button_frame, text="Calculate", command=simple_interest_calculator)
calculate_button.grid(row=0,column=0,padx=5,pady=5)


clear_button = ttk.Button(button_frame, text="Clear", command= clear)
clear_button.grid(row=0,column=1,padx=5,pady=5)

quit_button = ttk.Button(button_frame, text="Quit")
quit_button.grid(row=0,column=2,padx=5,pady=5)

root.mainloop()
